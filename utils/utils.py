from openai import OpenAI
from ollama import chat
from utils.prompt_loader import get_prompt
from utils.user_prompt_loader import get_user_prompt
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


def build_website_summary_prompt(website):
    template = get_user_prompt("website_summary")
    user_prompt = template.format(title=website.title, text=website.text)
    return user_prompt


def build_website_summary_messages(website):
    system_prompt = get_prompt("website_analysis")
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": build_website_summary_prompt(website)}
    ]

def summarize(url, method):
    website = WebsiteParser(url)
    if method == "OpenAI":
        openai = OpenAI()
        response = openai.chat.completions.create(
            model = "gpt-4o-mini",
            messages = build_website_summary_messages(website)
        )
        return response.choices[0].message.content
    elif method == "Ollama":
        response = chat(model=MODEL, messages=build_website_summary_messages(website))
        return response['message']['content']
    else:
        return "Please, select OpenAI or Ollama in your argument."

def display_summary(url, method):
    summary = summarize(url, method)
    display_markdown(summary)