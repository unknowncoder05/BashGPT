from llm_toolbox.chatgpt import ChatGptPetition
import subprocess
import os

os.chdir('sandbox')
def execute_commands(commands):
    try:
        output_list = []
        for command in commands:
            print(f"Executing: {command}")
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(f"Command executed successfully")
            output_list.append(result.stdout)
        return output_list
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        return str(e)
    except Exception as e:
        print(f"An error occurred: {e}")
        return str(e)

class CustomChatGptPetition(ChatGptPetition):
    def on_message(self, message):
        if message['role'] == 'function':
            log = f"{message['role']} {message['name']}: {message['content']}"
            print('internal>', log)
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
current_directory = os.getcwd()
contents = os.listdir(current_directory)
petition.system(
    "you are a software developer with the hability to execute any command on the terminal",
    "execute, read, create, delete or modify files if necesary",
    "solve the task even if not all the information was given",
    "if a first solution is not successful, try another way",
    "leave instructions of use if necessary",
    "do not use cd command",
    f"current_directory: {current_directory}",
    f"ls: {'/n'.join(contents)}",
)
petition.assistant(assistant_first_message)
petition.user(user_input)
petition.assistant("sure, here is what you have to do")

# execution
result = petition.execute()
