import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from .BaseLLMClient import BaseLLMClient

load_dotenv(override=True)

class AzureOpenAIClient(BaseLLMClient):
    def __init__(self):
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.api_key = os.getenv("AZURE_OPENAI_KEY")
        self.api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2025-03-01-preview")
        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

        if not all([self.endpoint, self.api_key, self.deployment_name]):
            raise ValueError("Missing one or more required Azure OpenAI environment variables.")

        self.client = AzureOpenAI(
            azure_endpoint=self.endpoint,
            api_key=self.api_key,
            api_version=self.api_version,
        )

    def generate_content(self, user_prompt: str) -> str:
        """Generate a chat completion response from Azure OpenAI."""
        messages = [{"role": "user", "content": user_prompt}]
        response = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
        )
        return response.choices[0].message.content.strip()

    def get_model_name(self) -> str:
        """Return the Azure deployment name as the model name."""
        return self.deployment_name