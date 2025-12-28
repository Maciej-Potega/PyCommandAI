#Setup frameworks
from langchain.tools import tool

#Tool-necessary frameworks
import datetime as dateT

@tool
def check_time() -> str:
    """Useful for checking the current system time"""
    current_time = dateT.datetime.now().strftime("%H:%M:%S")
    return f"The current local time is: {current_time}"