from utils.prompt_loader import get_prompt
from classes.OpenAIClient import OpenAIClient
from classes.ClaudeClient import ClaudeClient

gpt_model = "gpt-4o-mini"
claude_model = "claude-3-haiku-20240307"

gpt_system = get_prompt("adversarial_gpt")
claude_system = get_prompt("adversarial_claude")

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

def adversarial_conversation(turns=5, initial_message="Hi"):
    gpt_messages = [initial_message]
    claude_messages = [initial_message]
    for i in range(turns):
        gpt_next = call_gpt(gpt_messages, claude_messages)
        print(f"GPT:\n{gpt_next}\n")
        gpt_messages.append(gpt_next)

        claude_next = call_claude(claude_messages, gpt_messages)
        print(f"Claude:\n{claude_next}\n")
        claude_messages.append(claude_next)