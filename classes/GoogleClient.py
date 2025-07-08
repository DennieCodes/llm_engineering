import os
import google.generativeai

class GoogleClient:
    _system_message = "You are an LLM evangelist"
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
                model_name='gemini-2.0-flash',
                system_instruction=cls._system_message
            )
            cls._configured = True

    @classmethod
    def generate_content(cls, user_prompt):
        cls._auto_configure()
        return cls._gemini.generate_content(user_prompt)
