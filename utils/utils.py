from openai import OpenAI
from ollama import chat
from utils.prompt_loader import get_prompt
from utils.user_prompt_loader import get_user_prompt
from utils.parse_website import parse_website
from settings import MODEL

def display_markdown(text):
    print("\n" + "-" * 40)
    print(text)
    print("-" * 40 + "\n")
