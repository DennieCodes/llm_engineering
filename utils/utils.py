from openai import OpenAI
from ollama import chat
from prompts.website_analysis import system_prompt
from classes.WebsiteParser import WebsiteParser
from settings import MODEL

def display_markdown(text):
    print("\n" + "-" * 40)
    print(text)
    print("-" * 40 + "\n")

def check_api_key(api_key):
    if not api_key:
        return "No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!"
    elif not api_key.startswith("sk-proj-"):
        return "An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook"
    elif api_key.strip() != api_key:
        return "An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook"
    else:
        return "API key found and looks good so far!"

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