import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from openai import OpenAI
from utils import display_markdown, check_api_key

# display_markdown("### Title")

# load_dotenv(override=True)
# api_key = os.getenv('OPENAI_API_KEY')

# Test the OpenAI API
# openai = OpenAI()
# message = "Hello, GPT! This is my first ever message to you! Hi!"
# response = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user", "content":message}])
# print(response.choices[0].message.content)
