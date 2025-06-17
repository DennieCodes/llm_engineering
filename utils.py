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