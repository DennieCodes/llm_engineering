import os
from dotenv import load_dotenv
import anthropic
from .BaseLLMClient import BaseLLMClient

load_dotenv(override=True)
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')

class ClaudeClient(BaseLLMClient):
	_claude = anthropic.Anthropic()
	_model = "claude-3-7-sonnet-latest"

	def generate_content(self, user_prompt, system_message=None):
		# system_message is optional; Claude API allows omitting it
		kwargs = {
			"model": self._model,
			"max_tokens": 200,
			"temperature": 0.7,
			"messages": user_prompt
		}
		if system_message:
			kwargs["system"] = system_message
		return self._claude.messages.create(**kwargs)

	def get_model_name(self):
		return self._model