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
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")
assistant_first_message = "Hi! in which task can I assist you with?"
user_input = os.getenv('USER_INPUT')
print("user_input:", user_input)
petition = ChatGptPetition()
petition.add_function(
    execute_commands,
    "execute_commands",
    "execute commands on the console",
    {
        "commands": {"type": "array", "items": {"type": "string"}, "minItems": 1},
    },
)

# context
petition.system("you are an assistant with the hability to execute commands on a terminal")
petition.assistant(assistant_first_message)
petition.user(user_input)

# execution
result = petition.execute()
print("llm toolbox", result)
