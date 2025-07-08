from openai import OpenAI

class OpenAIClient:
    _openai = OpenAI()

    @classmethod
    def chat_completion(cls, message, model="gpt-4o-mini"):
        return cls._openai.chat.completions.create(
            model=model,
            messages=message
        )