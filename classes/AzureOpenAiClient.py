from openai import AzureOpenAI
from .BaseLLMClient import BaseLLMClient

class AzureOpenAIClient(BaseLLMClient):
    _model = ""
    _azureOpenAi = AzureOpenAI()
    # client = AzureOpenAI(
    # azure_endpoint=endpoint,
    # azure_ad_token_provider=token_provider,
    # api_version="2024-05-01-preview",
    # )

    def generate_content(self, user_prompt, system_message=None):
        messages = user_prompt.copy() if isinstance(user_prompt, list) else [user_prompt]

        if system_message:
            # Insert system message at the start if provided
            messages = [{"role": "system", "content": system_message}] + messages
        return self.__azureOpenAi.chat.completions.create(
            model=self._model,
            messages=messages
        )