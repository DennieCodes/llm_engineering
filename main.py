from classes.OpenAIClient import OpenAIClient
from classes.ClaudeClient import ClaudeClient

# messages = [
#         {"role": "system", "content": "You are an life coach and motivational speaker."},
#         {"role": "user", "content": "Please give me some encouraging words for today."}
#     ]

# openAiClient = OpenAIClient.chat_completion(messages);
# print(openAiClient);

claudeClientResponse = ClaudeClient.create_messages("Tell me about some leading AI developments")
print(claudeClientResponse)