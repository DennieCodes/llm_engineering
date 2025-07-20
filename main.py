from classes.AzureOpenAiClient import AzureOpenAIClient

def main():
    try:
        client = AzureOpenAIClient()
        response = client.generate_content("Say hello to the world in a fun way.")
        print("✅ AzureOpenAI Response:")
        print(response)
    except Exception as e:
        print("❌ Error communicating with Azure OpenAI:")
        print(e)

main()