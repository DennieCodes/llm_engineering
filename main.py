# from classes.GoogleClient import GoogleClient
# from utils.index import display_markdown

# user_prompt = "Tell me about the latest in LLM developments"
# formatted_content = display_markdown(GoogleClient.generate_content(user_prompt))
# print(formatted_content)

from utils.adversaries import call_gpt,call_claude

# print(call_claude())

gpt_messages = ["Hi there"]
claude_messages = ["Hi"]

for i in range(5):
    gpt_next = call_gpt(gpt_messages, claude_messages)
    print(f"GPT:\n{gpt_next}\n")
    gpt_messages.append(gpt_next)

    claude_next = call_claude(claude_messages, gpt_messages)
    print(f"Claude:\n{claude_next}\n")
    claude_messages.append(claude_next)