import os
from dotenv import load_dotenv
from openai import OpenAI
from .BaseLLMClient import BaseLLMClient

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')

class OpenAIClient(BaseLLMClient):
    _openai = OpenAI()
    _model = "gpt-4o-mini"
    _stream = False

    def generate_content(self, user_prompt, system_message=None):
        # user_prompt should be a list of messages as per OpenAI API
        messages = user_prompt.copy() if isinstance(user_prompt, list) else [user_prompt]
        if system_message:
            # Insert system message at the start if provided
            messages = [{"role": "system", "content": system_message}] + messages

        return self._openai.chat.completions.create(
            model=self._model,
            messages=messages
        )

    def set_stream_true(self):
        self._stream = True

    def get_model_name(self):
        return self._model