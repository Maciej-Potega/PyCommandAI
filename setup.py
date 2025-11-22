import os
from google import genai
from langchain_google_genai import ChatGoogleGenerativeAI # Enables the use of Gemini models (e.g., Gemini) within LangChain.
from langgraph.prebuilt import create_react_agent # Creates a ready-to-use ReAct agent that can reason and act step by step.
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv # Loads environment variables from a .env file (e.g., API keys or project configuration).
#from langchain.memory import ChatMessageHistory as history

#My imports
from custom_tools import plugins_loaded

#AI model name setup
AI_MODEL_NAME = "gemini-2.5-flash-lite"

#API Setup
load_dotenv()
API_KEY_NAME = "GOOGLE_API_KEY"
GOOGLE_API_KEY = os.getenv(API_KEY_NAME)

#Explain to Langchain how it should behave every time it gets an input from user
RULES_FOR_LANGCHAIN = (
    "You are a helpful conversational AI assistant. "
    "If a user asks something that requires a specific action, use the relevant tool. "
    "If no suitable tool exists, you must still respond normally using your general knowledge. "
    "Never say that you cannot help unless the question is about real-world people or restricted topics."
)

CHAT_CONTENT_FILE = "chat_file.txt"

model_active = {"active": False}

def Model_Setup():
    
    os.system('cls')

    if not GOOGLE_API_KEY:
        raise ValueError("API key not found in .env file!")

    print("Google API key found!")

    try:
        genai.Client(api_key=GOOGLE_API_KEY)
    except Exception as e:
        print(f"⚠️ Could not verify Gemini API key: {e}")
        
    if(plugins_loaded["loaded"]):

        from custom_tools import active_tools
        global agent_executor
        
        model = ChatGoogleGenerativeAI(temperature=0, model=AI_MODEL_NAME, google_api_key=GOOGLE_API_KEY) #Temperature 0 to make sure we don't want it to be any randomness
        custom_prompt = ChatPromptTemplate.from_messages([("system", RULES_FOR_LANGCHAIN),("human", "{messages}")])
        agent_executor = create_react_agent(model=model, tools=active_tools, prompt=custom_prompt)
    
        model_active["active"] = True

def Chat_Setup():
    if not os.path.exists(CHAT_CONTENT_FILE) or os.path.getsize(CHAT_CONTENT_FILE) == 0:
        with open(CHAT_CONTENT_FILE, mode="w") as chat_file:
            print("\nHi user! I am your personal AI agent that can answer your questions!")
            print("If you've like to quit, tell the agent to do so!")
    else:
        with open(CHAT_CONTENT_FILE, mode="r") as chat_file:
            chat_history = chat_file.read()
            print(chat_history)

Model_Setup()
Chat_Setup()



