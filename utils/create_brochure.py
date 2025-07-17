from utils.prompt_loader import get_prompt
from utils.user_prompt_loader import get_user_prompt
from utils.get_all_details import get_all_details
from settings import MODEL4o
from openai import OpenAI
from utils.index import display_markdown

openai = OpenAI()

def get_brochure_user_prompt(company_name, url):
    template = get_user_prompt("brochure")
    details = get_all_details(url)
    user_prompt = template.format(company_name=company_name, details=details)
    user_prompt = user_prompt[:5_000] # Truncate if more than 5,000 characters
    return user_prompt

def create_brochure(company_name, url):
    system_prompt = get_prompt("website_brochure")
    response = openai.chat.completions.create(
        model=MODEL4o,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ],
    )
    result = response.choices[0].message.content
    display_markdown(result)