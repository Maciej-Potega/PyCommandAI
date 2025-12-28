#Setup frameworks
from langchain.tools import tool

#Tool-necessary frameworks

end_chat = {"quit": False}

@tool
def exit_chat() -> str:
    """Useful if the user wants to end the chat (or say something like: Goodbye, bye, exit, quit, see you later, etc.)"""
    global end_chat
    end_chat["quit"] = True
    return "Goodbye user!"