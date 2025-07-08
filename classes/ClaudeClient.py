import anthropic

class ClaudeClient:
	_claude = anthropic.Anthropic()

	_system_message = "You are a technological evangelist."

	@classmethod
	def create_messages(cls, user_prompt):
		return cls._claude.messages.create(
			model="claude-3-7-sonnet-latest",
			max_tokens=200,
			temperature=0.7,
			system=cls._system_message,
			messages=[
				{"role": "user", "content": user_prompt},
			],
		)