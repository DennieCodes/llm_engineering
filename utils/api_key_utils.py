from openai import OpenAI
from settings import get_open_api_key, get_google_api_key, get_anthropic_api_key, get_azure_openai_api_key

def check_api_key():
    openai_api_key = get_open_api_key()
    if openai_api_key:
        print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
    else:
        print("OpenAI API Key not set")

    anthropic_api_key = get_anthropic_api_key()
    if anthropic_api_key:
        print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
    else:
        print("Anthropic API Key not set")

    google_api_key = get_google_api_key()
    if google_api_key:
        print(f"Google API Key exists and begins {google_api_key[:8]}")
    else:
        print("Google API Key not set")

    azure_openai_api_key = get_azure_openai_api_key()
    if azure_openai_api_key:
        print(f"Azure OpenAI API Key exists and begins {azure_openai_api_key[:8]}")
    else:
        print("Azure OpenAI API Key not set")

def test_OpenAI_API():
    try:
        openai = OpenAI()
        message = "Hello, GPT! This is my first ever message to you! Hi!"
        response = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user", "content":message}])
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred while testing the OpenAI API: {e}"
