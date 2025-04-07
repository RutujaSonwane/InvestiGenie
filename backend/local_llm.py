from gpt4all import GPT4All
import os

# Set correct model path
model_name = "gpt4all-falcon-newbpe-q4_0.gguf"
model_path = os.path.join("models", model_name)

# ✅ Make sure this path is correct: E:\college\...\models\gpt4all-falcon-newbpe-q4_0.gguf
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found at: {model_path}")

model = GPT4All(model_name=model_name, model_path="models", allow_download=False)

def generate_response_from_llm(prompt):
    response = model.generate(prompt, max_tokens=200, temp=0.7)
    return response
