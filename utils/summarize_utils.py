from openai import OpenAI
from ollama import chat
from utils.system_prompt_loader import get_prompt
from utils.user_prompt_loader import get_user_prompt
from utils.parse_website import parse_website
from settings import MODEL
from utils.display_markdown import display_markdown

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
    website = parse_website(url)
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
