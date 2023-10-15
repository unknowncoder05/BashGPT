from llm_toolbox.chatgpt import ChatGptPetition
import subprocess
import os


def execute_commands(commands):
    try:
        for command in commands:
            # Use subprocess.run to execute the command
            print(f"Executing: {command}")
            subprocess.run(command, shell=True, check=True)
            print(f"Command executed successfully")
    except subprocess.CalledProcessError as e:
        # Handle errors if the command fails
        print(f"Command failed: {e}")
        return str(e)
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")
        return str(e)

class CustomChatGptPetition(ChatGptPetition):
    def on_message(self, message):
        if message['role'] == 'function':
            log = f"{message['role']} {message['name']}: {message['content']}"
            print(log)
        else:
            log = f"{message['role']}: {message['content']}"
            print(log)


assistant_first_message = os.getenv("ASSISTANT_INITIAL_MESSAGE", "Hi! in which task can I assist you with?")
user_input = os.getenv("USER_INPUT")

petition = CustomChatGptPetition()
petition.add_function(
    execute_commands,
    "execute_commands",
    "execute commands on the console",
    {
        "commands": {"type": "array", "items": {"type": "string"}, "minItems": 1},
    },
)

# context
petition.system(
    "you are an software developer with the hability to execute any command on the terminal",
    "read, create, delete or modify files if necesary",
    "solve the task even if not all the information was given",
    "leave instructions if necessary",
    "do not use cd command",
)
petition.assistant(assistant_first_message)
petition.user(user_input)
petition.assistant("sure, here is what you have to do")

# execution
result = petition.execute()
