
from utils.index import create_brochure

def test_create_brochure_anthropic():
    company_name = "Anthropic"
    url = "https://www.anthropic.com/"
    try:
        brochure = create_brochure(company_name, url)
        print("Brochure:\n", brochure)
    except Exception as e:
        print("Error during create_brochure test:", e)

test_create_brochure_anthropic()
