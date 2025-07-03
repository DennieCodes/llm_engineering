import os
from dotenv import load_dotenv

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')

def get_open_api_key():
  return openai_api_key

def get_anthropic_api_key():
  return anthropic_api_key

def get_google_api_key():
  return google_api_key

headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"
MODEL4o = 'gpt-4o-mini'