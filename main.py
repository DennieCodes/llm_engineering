from utils.index import create_brochure
# from utils.get_links import get_links, get_links_user_prompt
# from utils.index import display_markdown

def test_create_brochure_anthropic():
    company_name = "Anthropic"
    url = "https://www.anthropic.com/"
    try:
        brochure = create_brochure(company_name, url)
        print("Brochure:\n", brochure)
    except Exception as e:
        print("Error during create_brochure test:", e)

test_create_brochure_anthropic()

# result = get_links("https://www.anthropic.com/")
# print(display_markdown(result))