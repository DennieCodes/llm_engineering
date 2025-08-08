import gradio as gr
from typing import List, Dict, Any, Optional, Generator
from .OpenAIClient import OpenAIClient
from .ClaudeClient import ClaudeClient
from utils.system_prompt_loader import get_prompt

"""
A comprehensive Gradio client library for building LLM-powered UI components.
Provides easy-to-use functions for different models and UI experiences.
"""
class GradioClient:
    def __init__(self, system_prompt_name: str = "useful_assistant"):

        self.system_message = get_prompt(system_prompt_name)
        self.openai_client = OpenAIClient()
        self.claude_client = ClaudeClient()

    def message_gpt(self, user_prompt: str) -> str:
        messages = [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": user_prompt}
        ]
        response = self.openai_client.generate_content(messages)
        return response.choices[0].message.content

    def stream_gpt(self, user_prompt: str) -> Generator[str, None, None]:
        self.openai_client.set_stream_true()
        messages = [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": user_prompt}
        ]
        try:
            stream = self.openai_client.generate_content(user_prompt=messages)
            for chunk in stream.choices:
                content = chunk.message.content
                if content:
                    yield content
        except Exception as e:
            yield f"❌ Error: {str(e)}"

    def stream_claude(self, user_prompt: str) -> Generator[str, None, None]:
        messages = [
            {"role": "user", "content": user_prompt}
        ]
        try:
            result = self.claude_client.generate_content(
                user_prompt=messages,
                system_message=self.system_message
            )
            response = ""
            with result as stream:
                for text in stream.text_stream:
                    response += text or ""
                    yield response
        except Exception as e:
            yield f"❌ Error: {str(e)}"

    def create_chat_interface(self,
                            model: str = "gpt",
                            streaming: bool = True,
                            title: str = "AI Chat Assistant",
                            description: str = "Chat with different AI models") -> gr.Interface:

        if model.lower() == "gpt":
            fn = self.stream_gpt if streaming else self.message_gpt
        elif model.lower() == "claude":
            fn = self.stream_claude
        else:
            raise ValueError(f"Unsupported model: {model}")

        return gr.Interface(
            fn=fn,
            inputs=[gr.Textbox(label="Your message:", placeholder="Type your message here...")],
            outputs=[gr.Markdown(label="Response:")],
            title=title,
            description=description,
            flagging_mode="never"
        )

    def create_multi_model_interface(self) -> gr.Interface:
        def chat_with_model(message: str, model: str, streaming: bool) -> str:
            if model == "GPT":
                if streaming:
                    return self.stream_gpt(message)
                else:
                    return self.message_gpt(message)
            elif model == "Claude":
                return self.stream_claude(message)
            else:
                return "❌ Unsupported model"

        return gr.Interface(
            fn=chat_with_model,
            inputs=[
                gr.Textbox(label="Your message:", placeholder="Type your message here..."),
                gr.Dropdown(choices=["GPT", "Claude"], value="GPT", label="Model"),
                gr.Checkbox(label="Streaming", value=True)
            ],
            outputs=[gr.Markdown(label="Response:")],
            title="Multi-Model AI Chat",
            description="Chat with different AI models",
            flagging_mode="never"
        )

    def create_parameterized_interface(self,
                                    temperature: float = 0.7,
                                    max_tokens: int = 200) -> gr.Interface:
        # Note: This would require extending the client classes to support parameters
        def chat_with_params(message: str, temp: float, tokens: int) -> str:
            # For now, return a basic response
            return f"Temperature: {temp}, Max Tokens: {tokens}\n\n{self.message_gpt(message)}"

        return gr.Interface(
            fn=chat_with_params,
            inputs=[
                gr.Textbox(label="Your message:", placeholder="Type your message here..."),
                gr.Slider(minimum=0.0, maximum=2.0, value=temperature, label="Temperature"),
                gr.Slider(minimum=50, maximum=1000, value=max_tokens, label="Max Tokens")
            ],
            outputs=[gr.Markdown(label="Response:")],
            title="Parameterized AI Chat",
            description="Chat with adjustable parameters",
            flagging_mode="never"
        )

    def create_file_upload_interface(self) -> gr.Interface:
        def analyze_file(file, message: str) -> str:
            if file is None:
                return "Please upload a file first."

            # Basic file analysis - can be extended based on file type
            file_info = f"File: {file.name}, Size: {file.size} bytes\n\n"
            analysis = self.message_gpt(f"Analyze this file and answer: {message}\n\nFile info: {file_info}")
            return file_info + analysis

        return gr.Interface(
            fn=analyze_file,
            inputs=[
                gr.File(label="Upload a file for analysis"),
                gr.Textbox(label="Your question:", placeholder="What would you like to know about this file?")
            ],
            outputs=[gr.Markdown(label="Analysis:")],
            title="File Analysis Assistant",
            description="Upload files and ask questions about them",
            flagging_mode="never"
        )

    def launch_interface(self,
                        interface_type: str = "chat",
                        **kwargs) -> None:
        """
        Launch a specific type of interface.

        Args:
            interface_type (str): Type of interface to launch
            **kwargs: Additional arguments for the interface
        """
        if interface_type == "chat":
            interface = self.create_chat_interface(**kwargs)
        elif interface_type == "multi_model":
            interface = self.create_multi_model_interface()
        elif interface_type == "parameterized":
            interface = self.create_parameterized_interface(**kwargs)
        elif interface_type == "file_upload":
            interface = self.create_file_upload_interface()
        else:
            raise ValueError(f"Unsupported interface type: {interface_type}")

        interface.launch()


# Example usage and testing
if __name__ == "__main__":
    # Create a GradioClient instance
    client = GradioClient()

    # Launch a simple chat interface
    client.launch_interface("chat", model="gpt", streaming=True)
