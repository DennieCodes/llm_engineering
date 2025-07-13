from prompts.adversaries import gpt_system, claude_system
from classes.OpenAIClient import OpenAIClient
from classes.ClaudeClient import ClaudeClient

gpt_model = "gpt-4o-mini"
claude_model = "claude-3-haiku-20240307"

def call_gpt(gpt_messages, claude_messages):
    messages = [{"role": "system", "content": gpt_system}]
    for gpt, claude in zip(gpt_messages, claude_messages):
        messages.append({"role": "assistant", "content": gpt})
        messages.append({"role": "user", "content": claude})
    completion = OpenAIClient.chat_completion(
        model=gpt_model,
        message=messages
    )
    return completion.choices[0].message.content

def call_claude(claude_messages, gpt_messages):
    messages = []
    for gpt, claude_message in zip(gpt_messages, claude_messages):
        messages.append({"role": "user", "content": gpt})
        messages.append({"role": "assistant", "content": claude_message})
    messages.append({"role": "user", "content": gpt_messages[-1]})
    message = ClaudeClient.create_messages(
        model=claude_model,
        system_message=claude_system,
        user_prompt=messages,
    )
    return message.content[0].text