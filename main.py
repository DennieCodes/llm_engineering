from utils.utils import display_markdown, test_OpenAI_API
from settings import get_api_key, get_headers
from utils.WebsiteParser import WebsiteParser

api_key = get_api_key()
# headers = get_headers()

url = "https://denniecodes.com"
parser = WebsiteParser(url)
print(parser.title)
print(parser.text)
