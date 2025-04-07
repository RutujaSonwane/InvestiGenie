import React, { useState } from "react";
import axios from "axios";
import "./Chat.css"; // Optional, for styling

const Chat = () => {
  const [messages, setMessages] = useState([
    { text: "Hi! I’m InvestiGenie 💰, your AI Investment Buddy. Ask me anything!", sender: "bot" }
  ]);
  const [userInput, setUserInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSend = async () => {
    if (!userInput.trim()) return;

    const userMessage = { text: userInput, sender: "user" };
    setMessages((prev) => [...prev, userMessage]);
    setIsLoading(true);

    try {
      const res = await axios.post("http://localhost:5000/query", {
        question: userInput
      });

      const botMessage = {
        text: res.data.answer,
        sender: "bot"
      };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { text: "Sorry, I couldn't process that. Try again later.", sender: "bot" }
      ]);
      console.error("Error:", error);
    }

    setUserInput("");
    setIsLoading(false);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`chat-message ${msg.sender === "user" ? "user" : "bot"}`}
          >
            {msg.text}
          </div>
        ))}
        {isLoading && <div className="chat-message bot">Typing...</div>}
      </div>
      <div className="input-container">
        <input
          type="text"
          placeholder="Ask about SIPs, FD, stocks..."
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
};

export default Chat;
