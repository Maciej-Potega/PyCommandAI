# 🤖 AI Command-Line Assistant

**A lightweight terminal AI powered by LangChain + tool calling**

This project is a simple but powerful example of how to build an AI assistant that works **directly in the command line**.
It supports **streaming responses**, **function calling**, and **custom tools** that allow the **AI to perform real actions**.

Perfect as a learning project, a base for your own AI assistant, or a reference for LangChain tool integration.

---

# 🧠 Features

* ✔️ Real-time streaming output
* ✔️ Persistent conversation history
* ✔️ Tool/function calling support
* ✔️ Custom Python functions the AI can execute
* ✔️ Clean modular structure
* ✔️ Easy to extend with new tools

---

# ⚙️ How It Works

The system is built around a LangChain Agent using function calling.
When the user sends input:

1. The model decides whether to answer normally or call a tool

2. If a tool is called → the Python function is executed

3. The result is streamed back to the user

4. The conversation is appended to chat_content.txt

Example Tool:
```python 
def say_hello(name): 
  return f"Hello, {name}!" 
``` 

---

# 🛠️ Currently Tools Available:

🔹 say_hello(name: str)

Greets the user with a friendly message.

🔹 check_time()

Returns the current system time.

🔹 exit_chat()

Sets a flag to safely end the chat loop.

---

# 🚀 Getting Started

1️⃣ Install following dependencies:

⚠️ IMPORTANT - All the dependencie were installed using UV instead of pip

- uv add (List of the dependencies)

2️⃣ Add your API key:

Create a .env file inside the project folder:

- GOOGLE_API_KEY=your_key_here

3️⃣ Run the assistant:

- uv run main.py

# 🧪 Example Session

* You: What time is it?

* Assistant: The current local time is 18:58:50

* You: Say hello to Maciej

* Assistant: Hi Maciej! I hope you're doing well today!

* You: quit

* Assistant: Goodbye user!

---

# 📅 Roadmap / Future Ideas

 * Note-taking tool

 * File-reading tool

 * System info tool

 * Math/calc tool

 * Joke generator tool

 * Mini-games (coin flip, dice roll)

 * Local model support (Ollama)

 * Memory embeddings



