from classes.WebsiteLinksScraper import Website
# from settings import get_api_key
from prompts.website_scraper import link_system_prompt
from utils.get_links import get_links
# api_key = get_api_key()

# den = Website("https://denniecodes.com")
# print(den.links)

# print(link_system_prompt)
# print(get_links_user_prompt(den))
huggingface = Website("https://huggingface.co")
huggingface.links
results = get_links(huggingface.url)
print(results)
