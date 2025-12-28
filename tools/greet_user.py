#Setup frameworks
from langchain.tools import tool

#Tool-necessary frameworks

@tool
def greet_user(name: str) -> str:
    """Useful for greeting a user"""
    return f"Hi {name}! I hope you're doing well today!"

 