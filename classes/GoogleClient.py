import os
import google.generativeai
from .BaseLLMClient import BaseLLMClient

class GoogleClient(BaseLLMClient):
    _gemini = None
    _configured = False

    @classmethod
    def _auto_configure(cls):
        if not cls._configured:
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                raise RuntimeError("GOOGLE_API_KEY environment variable not set.")
            google.generativeai.configure(api_key=api_key)
            cls._gemini = google.generativeai.GenerativeModel(
                model_name='gemini-2.0-flash'
            )
            cls._configured = True

    def generate_content(self, user_prompt, system_message=None):
        self._auto_configure()
        if system_message:
            # Create a new model instance with the custom system message
            temp_model = google.generativeai.GenerativeModel(
                model_name='gemini-2.0-flash',
                system_instruction=system_message
            )
            return temp_model.generate_content(user_prompt)
        else:
            return self._gemini.generate_content(user_prompt)

    def get_model_name(self):
        return 'gemini-2.0-flash'
