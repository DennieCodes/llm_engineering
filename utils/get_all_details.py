from classes.WebsiteLinksScraper import WebsiteLinkScraper
from utils.get_links import get_links

def get_all_details(url):
    result = "Landing page:\n"
    result += WebsiteLinkScraper(url).get_contents()
    links = get_links(url)
    print("Found links:", links)
    for link in links["links"]:
        result += f"\n\n{link['type']}\n"
        result += WebsiteLinkScraper(link["url"]).get_contents()
    return result