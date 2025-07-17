from openai import OpenAI
from ollama import chat
from utils.prompt_loader import get_prompt
from classes.WebsiteParser import WebsiteParser
from settings import MODEL
from settings import get_open_api_key, get_google_api_key, get_anthropic_api_key

def display_markdown(text):
    print("\n" + "-" * 40)
    print(text)
    print("-" * 40 + "\n")

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

def test_OpenAI_API():
    try:
        openai = OpenAI()
        message = "Hello, GPT! This is my first ever message to you! Hi!"
        response = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user", "content":message}])
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred while testing the OpenAI API: {e}"

def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
        please provide a short summary of this website in markdown. \
        If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

def messages_for(website):
    system_prompt = get_prompt("website_analysis")
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

def summarize(url, method):
    website = WebsiteParser(url)
    if method == "OpenAI":
        openai = OpenAI()
        response = openai.chat.completions.create(
            model = "gpt-4o-mini",
            messages = messages_for(website)
        )
        return response.choices[0].message.content
    elif method == "Ollama":
        response = chat(model=MODEL, messages=messages_for(website))
        return response['message']['content']
    else:
        return "Please, select OpenAI or Ollama in your argument."

def display_summary(url, method):
    summary = summarize(url, method)
    display_markdown(summary)