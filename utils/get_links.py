from utils.index import scrape_website_links
from openai import OpenAI
from settings import MODEL4o
from utils.prompt_loader import get_prompt
from utils.user_prompt_loader import get_user_prompt
import json

openai = OpenAI()

def get_links_user_prompt(website):
    template = get_user_prompt("links")
    user_prompt = template.format(url=website.url, links="\n".join(website.links))
    return user_prompt

def get_links(url):
    website = scrape_website_links(url)
    link_system_prompt = get_prompt("link_system_prompt")
    response = openai.chat.completions.create(
        model=MODEL4o,
        messages=[
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": get_links_user_prompt(website)}
        ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    return json.loads(result)