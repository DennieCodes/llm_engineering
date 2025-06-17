from openai import OpenAI

def display_markdown(text):
    print("\n" + "-" * 40)
    print(text)
    print("-" * 40 + "\n")

def check_api_key(api_key):
    if not api_key:
        return "No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!"
    elif not api_key.startswith("sk-proj-"):
        return "An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook"
    elif api_key.strip() != api_key:
        return "An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook"
    else:
        return "API key found and looks good so far!"

def test_OpenAI_API():
    try:
        openai = OpenAI()
        message = "Hello, GPT! This is my first ever message to you! Hi!"
        response = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user", "content":message}])
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred while testing the OpenAI API: {e}"

class Website:

    def __init__(self, url):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)
