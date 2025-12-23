# 🤖 AI Command-Line Assistant

**A lightweight terminal AI powered by LangChain + tool calling**

This project is a simple but powerful example of how to build an AI assistant that works **directly in the command line**.
It supports **streaming responses**, **function calling**, and **custom tools** that allow the **AI to perform real actions**.

Perfect as a learning project, a base for your own AI assistant, or a reference for LangChain tool integration.

---

## 🧠 Features

✔️ **Real-time streaming output**   
✔️ **Persistent conversation history**   
✔️ **Tool/function calling support**   
✔️ **Custom Python functions the AI can execute**   
✔️ **Clean modular structure**   
✔️ **Easy to extend with new tools**

---

## ⚙️ How It Works

The system is **built around Gemini API (for now) with LangChain Agent using function calling**.
When the user sends input:

**1. The model decides whether to answer normally or call a tool**

**2. If a tool is called → the Python function is executed**

**3. The result is streamed back to the user**

**4. The conversation is appended to chat_file.txt (Which is automatically created when executed script for the first time or if file is not detected in the project directory)**

Example Tool:
```python 
@tool
def say_hello(name: str) -> str:
    """Useful for greeting a user"""
    #print("(Greeting) tool has been called!")
    return f"Hi {name}! I hope you're doing well today!\n" 
```
---

## 🛠️ Currently Tools Available:

**🔹 say_hello(name: str)**

Greets the user with a friendly message.

**🔹 check_time()**

Returns the current system time.

**🔹 exit_chat()**

Sets a flag to safely end the chat loop.

---

## 🚀 Getting Started

### 1️⃣ Download & navigate to the project directory:

```bash
your_drive:\your_directory\...\PyCommandAI
```
**OR**

### Clone the repository:
```bash
git clone https://github.com/Maciej-Potega/PyCommandAI.git
```

### 2️⃣ Install following dependencies with terminal:

```bash
pip install langgraph langchain langchain-google-genai google-generativeai google-api-core python-dotenv
```

### 3️⃣ Add your API key:

Create a .env file inside the project folder:

```env
GOOGLE_API_KEY=your_key_here
```

**Where do I get Google API key?**

1. Navigate to [Google AI Studio](https://aistudio.google.com/app/api-keys)
2. Click `Create API key` button
3. Select `Create Project` and name your project
4. Click `Create API key` button once more
5. **Select your project**, **name your API key** & click `Create key`
6. Copy and paste the key inside **.env file**


### 4️⃣ Run the assistant with terminal:

```python
python main.py
```
---

## 🧪 Example Session

```txt
You: What time is it?

Assistant: The current local time is 18:58:50

You: Say hello to Maciej

Assistant: Hi Maciej! I hope you're doing well today!

You: quit

Assistant: Goodbye user!
```
---

## ⚠️ Help! My request limit expired! What do I do?

In `setup.py` replace variable `AI_MODEL_NAME` with a different model name: 

For example:
```python
AI_MODEL_NAME = "gemini-2.5-flash-lite"
```

Where do I find different model names?

You can find them either on [Google AI Studio](https://aistudio.google.com/app/usage?timeRange=this-month) - in **"Rate Limit"** section OR [Firebase](https://firebase.google.com/docs/ai-logic/models) (better model descriptions)

---

## 📅 Roadmap / Future Ideas

### 🎯 Priorities 
 
 * **File-reading tool**

 * **System info tool**
 
 * **Note-taking tool**

 * **Math/calc tool**

 * **Local model support (f.e Ollama)**

 * **Memory embeddings (extend it's quality and stability)**

 * **GUI Support**

### 🎉 4FUN Utilities

 * **Joke generator tool**

 * **Mini-games (coin flip, dice roll etc.)**
   
 



