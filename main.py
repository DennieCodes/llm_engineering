from utils.utils import display_summary
from settings import get_api_key, get_headers
# from utils.WebsiteParser import WebsiteParser

api_key = get_api_key()

url = "https://denniecodes.com"
# parsed_website = WebsiteParser(url)

display_summary(url)
