from llm_toolbox.chatgpt import ChatGptPetition

petition = ChatGptPetition()
petition.system("you are a llm toolbox assistant")
result = petition.execute(limit_calls=0)
print("llm toolbox", result)