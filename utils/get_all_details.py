from utils.index import scrape_website_links
from utils.get_links import get_links

def get_all_details(url):
    result = "Landing page:\n"
    details = scrape_website_links(url)
    result += f"Webpage Title:\n{details['title']}\nWebpage Contents:\n{details['text']}\n\n"
    links = get_links(url)
    print("Found links:", links)
    for link in links["links"]:
        result += f"\n\n{link['type']}\n"
        details = scrape_website_links(link["url"])
        result += f"Webpage Title:\n{details['title']}\nWebpage Contents:\n{details['text']}\n\n"
    return result