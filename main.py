from classes.GoogleClient import GoogleClient
from utils.index import display_markdown

user_prompt = "Tell me about the latest in LLM developments"
formatted_content = display_markdown(GoogleClient.generate_content(user_prompt))
print(formatted_content)
