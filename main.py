import json
from langchain_core.messages import HumanMessage # Represents a message from the user (human) sent to the language model.

#My imports
from setup import agent_executor, CHAT_CONTENT_FILE
from custom_tools import Execute_Tool_Function, end_chat


def Chat_With_AI():

    global end_chat

    while True:

        

        user_input = input("\nYou: ").strip()
        ai_response = ""

        print("\nAssistant: ", end="") #"end=" is used here for in order to python doesn't jump to the next line when responding the user.

        with open(CHAT_CONTENT_FILE, mode="r") as chat_file:
            chat_history = chat_file.read()

        send_message_content = [HumanMessage(content=f"Previous chat history:\n{chat_history}\n\nUser just said: {user_input}")]

        tool_executed = False

        #1. We want to "stream" what the output is based on our input. 2. "Chunks" are essentially PART OF A RESPONSE COMING FROM OUR AGENT
        for chunk in agent_executor.stream({"messages": send_message_content}):

            #print(chunk) <-- Debug how the agent makes decisions

            if "agent" in chunk and "messages" in chunk["agent"]:
                    
                for message in chunk["agent"]["messages"]:

                    func_call = message.additional_kwargs.get("function_call")

                    if(func_call is not None):

                        func_name = func_call.get("name")
                        func_args = json.loads(func_call.get("arguments", "{}") or "{}")

                        ai_response = Execute_Tool_Function(func_name, func_args)
                        tool_executed = True
                    
                    elif(not tool_executed):
                        ai_response = message.content
        
        print(ai_response)                
                        
        with open(CHAT_CONTENT_FILE, mode="a") as chat_file:

            chat_file.write(f"You: {user_input}\n\n")

            if(end_chat["quit"] == True):
                chat_file.write(f"Assistant: {ai_response}")
                break
            else:
                chat_file.write(f"Assistant: {ai_response}\n\n")

if __name__ == "__main__":
    Chat_With_AI()


