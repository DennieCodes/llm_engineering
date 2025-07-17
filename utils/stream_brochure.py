from settings import MODEL4o
from openai import OpenAI
from utils.prompt_loader import get_prompt
from utils.create_brochure import get_brochure_user_prompt
from utils.utils import display_markdown
from IPython.display import Markdown, display, update_display

openai = OpenAI()

def stream_brochure(company_name, url):

    system_prompt = get_prompt("website_brochure")
    stream = openai.chat.completions.create(
        model=MODEL4o,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ],
        stream=True
    )

    response = ""
    display_handle = display(Markdown(""), display_id=True)
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        response = response.replace("```","").replace("markdown", "")
        if display_handle and hasattr(display_handle, "display_id"):
            update_display(Markdown(response), display_id=display_handle.display_id)
        else:
            print(response)