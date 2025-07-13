import anthropic

class ClaudeClient:
	_claude = anthropic.Anthropic()

	_system_message = "You are a technological evangelist."
	_model = "claude-3-7-sonnet-latest"

	@classmethod
	def create_messages(cls, user_prompt, model=_model, system_message=_system_message):
		return cls._claude.messages.create(
			model=model,
			max_tokens=200,
			temperature=0.7,
			system=system_message,
			messages=user_prompt
		)