import gradio as gr
from classes.OpenAIClient import OpenAIClient
from classes.ClaudeClient import ClaudeClient
from utils.system_prompt_loader import get_prompt

system_message = get_prompt("useful_assistant")

def message_gpt(user_prompt):
    openAI = OpenAIClient()
    messages = [
        {"role" : "system", "content": system_message},
        {"role": "user", "content": user_prompt}]
    response = openAI.generate_content(messages)
    return response.choices[0].message.content

def stream_claude(user_prompt):
    claude = ClaudeClient()
    messages = [
        {"role": "user", "content": user_prompt}
    ]
    result = claude.generate_content(user_prompt=messages, system_message=system_message)
    with result as stream:
        for text in stream.text_stream:
            response += text or ""
            yield response

def stream_gpt(user_prompt):
    openAI = OpenAIClient()
    openAI.set_stream_true()
    messages = [
        {"role" : "system", "content": system_message},
        {"role": "user", "content": user_prompt}
    ]
    try:
        stream = openAI.generate_content(user_prompt=messages)
        for chunk in stream.choices:
            content = chunk.message.content
            if content:
                yield content
    except Exception as e:
        yield f"❌ Error: {str(e)}"

view = gr.Interface(
    fn=stream_claude,
    inputs=[gr.Textbox(label="Your message:")],
    outputs=[gr.Markdown(label="Response:")],
    flagging_mode="never")

view.launch()
