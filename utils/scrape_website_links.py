import requests
from bs4 import BeautifulSoup
from settings import headers

def scrape_website_links(url):
    response = requests.get(url, headers=headers)
    body = response.content
    soup = BeautifulSoup(body, 'html.parser')
    title = soup.title.string if soup.title else "No title found"
    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    links = [link.get('href') for link in soup.find_all('a')]
    links = [link for link in links if link]
    return {
        "title": title,
        "text": text,
        "links": links
    }
