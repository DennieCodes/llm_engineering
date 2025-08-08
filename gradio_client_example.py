#!/usr/bin/env python3
"""
Example usage of the GradioClient class.
This file demonstrates different ways to use the GradioClient library.
"""

from classes.GradioClient import GradioClient

def main():
    """Main function to demonstrate GradioClient usage."""

    # Create a GradioClient instance
    client = GradioClient(system_prompt_name="useful_assistant")

    print("GradioClient Examples")
    print("====================")
    print("1. Simple chat interface with GPT")
    print("2. Multi-model interface")
    print("3. Parameterized interface")
    print("4. File upload interface")
    print("5. Custom interface")

    # Example 1: Simple chat interface
    print("\n--- Example 1: Simple Chat Interface ---")
    chat_interface = client.create_chat_interface(
        model="gpt",
        streaming=True,
        title="GPT Chat Assistant",
        description="Chat with GPT-4 model"
    )

    # Example 2: Multi-model interface
    print("\n--- Example 2: Multi-Model Interface ---")
    multi_interface = client.create_multi_model_interface()

    # Example 3: Parameterized interface
    print("\n--- Example 3: Parameterized Interface ---")
    param_interface = client.create_parameterized_interface(
        temperature=0.8,
        max_tokens=300
    )

    # Example 4: File upload interface
    print("\n--- Example 4: File Upload Interface ---")
    file_interface = client.create_file_upload_interface()

    # Example 5: Custom interface using the core functions
    print("\n--- Example 5: Custom Interface ---")
    def custom_chat(message: str, use_gpt: bool = True):
        if use_gpt:
            return client.message_gpt(message)
        else:
            # For Claude, we need to handle streaming differently
            return "Claude response would go here"

    custom_interface = gr.Interface(
        fn=custom_chat,
        inputs=[
            gr.Textbox(label="Your message:", placeholder="Type your message here..."),
            gr.Checkbox(label="Use GPT", value=True)
        ],
        outputs=[gr.Markdown(label="Response:")],
        title="Custom Chat Interface",
        description="A custom interface using GradioClient functions"
    )

    # Launch one of the interfaces
    print("\nLaunching chat interface...")
    multi_interface.launch()


if __name__ == "__main__":
    import gradio as gr
    main()
