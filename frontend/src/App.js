import React, { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setResponse("");

    try {
      const res = await fetch("http://127.0.0.1:5000/query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query }),
      });

      if (!res.ok) {
        throw new Error("Failed to fetch");
      }

      const data = await res.json();
      setResponse(data.response || "No response found.");
    } catch (error) {
      console.error("Error fetching data:", error);
      setResponse("Something went wrong!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h1>InvestiGenie 💰</h1>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask a question like 'What is SIP?'"
        style={styles.input}
      />
      <button onClick={handleAsk} style={styles.button}>
        {loading ? "Asking..." : "Ask"}
      </button>
      <div style={styles.responseBox}>
        <strong>Response:</strong> <br />
        {response}
      </div>
    </div>
  );
}

const styles = {
  container: {
    maxWidth: "600px",
    margin: "auto",
    padding: "20px",
    fontFamily: "sans-serif",
    textAlign: "center",
  },
  input: {
    width: "100%",
    padding: "10px",
    fontSize: "16px",
    marginBottom: "10px",
  },
  button: {
    padding: "10px 20px",
    fontSize: "16px",
    cursor: "pointer",
  },
  responseBox: {
    marginTop: "20px",
    background: "#f0f0f0",
    padding: "15px",
    borderRadius: "8px",
    textAlign: "left",
  },
};

export default App;
