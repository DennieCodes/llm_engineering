from utils.get_links import get_links

# Test the refactored website_scraper prompt loading
url = "https://www.anthropic.com"
links = get_links(url)
print("Relevant links for brochure:")
print(links)