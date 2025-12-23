#Setup frameworks
import json
from langchain_core.messages import HumanMessage # Represents a message from the user (human) sent to the language model.
from google.api_core.exceptions import ResourceExhausted

#Local imports
from setup import AI_MODEL_NAME, model_active
if(model_active["active"]):
    from setup import agent_executor, CHAT_CONTENT_FILE
    from custom_tools import Execute_Tool_Function, end_chat

def Chat_With_AI():

    global AI_MODEL_NAME, end_chat

    while True:

        user_input = input("\nYou: ").strip()

        print("\nAssistant: ", end="") #"end=" is used here for in order to python doesn't jump to the next line when responding the user.

        with open(CHAT_CONTENT_FILE, mode="r") as chat_file:
            chat_history = chat_file.read()

        send_message_content = [HumanMessage(content=f"Previous chat history:\n{chat_history}\n\nUser just said: {user_input}")]

        tool_executed = False

        try:
            #1. We want to "stream" what the output is based on our input. 2. "Chunks" are essentially PART OF A RESPONSE COMING FROM OUR AGENT
            for chunk in agent_executor.stream({"messages": send_message_content}):

                #print(chunk) <-- Debug how the agent makes decisions

                if "agent" in chunk and "messages" in chunk["agent"]:
                    
                    for message in chunk["agent"]["messages"]:

                        func_call = message.additional_kwargs.get("function_call")

                        if func_call is not None:

                            func_name = func_call.get("name")
                            func_args = json.loads(func_call.get("arguments", "{}") or "{}")

                            ai_response = Execute_Tool_Function(func_name, func_args)
                            tool_executed = True
                    
                        elif not tool_executed:
                            ai_response = message.content
        
            print(ai_response) 

        except ResourceExhausted:
            print(f"⚠️ | Today's request limit for this specific AI-model ({AI_MODEL_NAME}) has expired!")
            print("\n✅ | Try to change to a different AI-model in setup.py file!\n")
            break
        
        with open(CHAT_CONTENT_FILE, mode="a") as chat_file:

            chat_file.write(f"You: {user_input}\n\n")

            if end_chat["quit"]:
                chat_file.write(f"Assistant: {ai_response}")
                break
            else:
                chat_file.write(f"Assistant: {ai_response}\n\n")

if __name__ == "__main__":
    Chat_With_AI()


