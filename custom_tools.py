from langchain.tools import tool # Allows creating custom “tools” (functions) that the agent can use.
from langchain_core.tools import StructuredTool
from sys import modules
from inspect import getmembers

import datetime as dateT

end_chat = {"quit": False}

@tool
def say_hello(name: str) -> str:
    """Useful for greeting a user"""
    return f"Hi {name}! I hope you're doing well today!"

@tool
def check_time() -> None:
    """Useful for checking the current system time"""
    return None

@tool
def exit_chat() -> None:
    """Useful if the user wants to end the chat (or say something like: Goodbye)"""
    return None

def LoadTools():
    
    current_module = modules[__name__]
    active_tools = []

    for name, obj in getmembers(current_module): # iterable variable "name" has to be here for some reason in order to make the model use custom tools xD

        if isinstance(obj, StructuredTool):
            active_tools.append(obj)
    
    return active_tools

plugins_loaded = {"loaded": False}
active_tools = LoadTools()
plugins_loaded["loaded"] = True


def Execute_Tool_Function(func_name: str, func_args: dict):

    global end_chat
    
    if func_name == "say_hello":
        return say_hello.invoke(func_args)
    
    elif func_name == "check_time":
        current_time = dateT.datetime.now().strftime("%H:%M:%S")
        return f"The current local time is: {current_time}"
    
    elif func_name == "exit_chat":
        end_chat["quit"] = True
        return "Goodbye user!"





