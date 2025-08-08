# GradioClient Class Documentation

The `GradioClient` class provides a comprehensive library for building LLM-powered UI components using Gradio. It abstracts the complexity of working with different AI models and provides easy-to-use functions for various UI experiences.

## Features

- **Multiple Model Support**: GPT and Claude models
- **Streaming Responses**: Real-time streaming for better user experience
- **Pre-built Interfaces**: Ready-to-use UI components
- **Extensible Design**: Easy to add new models and interface types
- **Error Handling**: Robust error handling for API calls

## Core Functions

### `message_gpt(user_prompt: str) -> str`
Generate a single response from GPT model.

```python
client = GradioClient()
response = client.message_gpt("Hello, how are you?")
print(response)
```

### `stream_gpt(user_prompt: str) -> Generator[str, None, None]`
Stream response from GPT model for real-time output.

```python
client = GradioClient()
for chunk in client.stream_gpt("Tell me a story"):
    print(chunk, end="", flush=True)
```

### `stream_claude(user_prompt: str) -> Generator[str, None, None]`
Stream response from Claude model for real-time output.

```python
client = GradioClient()
for chunk in client.stream_claude("Explain quantum computing"):
    print(chunk, end="", flush=True)
```

## Pre-built Interfaces

### 1. Chat Interface
Create a simple chat interface with any model.

```python
client = GradioClient()
interface = client.create_chat_interface(
    model="gpt",  # or "claude"
    streaming=True,
    title="AI Chat Assistant",
    description="Chat with AI models"
)
interface.launch()
```

### 2. Multi-Model Interface
Create an interface that allows switching between different models.

```python
client = GradioClient()
interface = client.create_multi_model_interface()
interface.launch()
```

### 3. Parameterized Interface
Create an interface with adjustable parameters (temperature, max tokens).

```python
client = GradioClient()
interface = client.create_parameterized_interface(
    temperature=0.8,
    max_tokens=300
)
interface.launch()
```

### 4. File Upload Interface
Create an interface for file analysis.

```python
client = GradioClient()
interface = client.create_file_upload_interface()
interface.launch()
```

## Quick Launch Methods

Use the `launch_interface` method for quick setup:

```python
client = GradioClient()

# Launch different interface types
client.launch_interface("chat", model="gpt", streaming=True)
client.launch_interface("multi_model")
client.launch_interface("parameterized", temperature=0.8)
client.launch_interface("file_upload")
```

## Custom Interfaces

You can create custom interfaces using the core functions:

```python
import gradio as gr
from classes.GradioClient import GradioClient

client = GradioClient()

def custom_chat(message: str, use_gpt: bool = True):
    if use_gpt:
        return client.message_gpt(message)
    else:
        return "Claude response"

interface = gr.Interface(
    fn=custom_chat,
    inputs=[
        gr.Textbox(label="Your message:"),
        gr.Checkbox(label="Use GPT", value=True)
    ],
    outputs=[gr.Markdown(label="Response:")],
    title="Custom Chat"
)
interface.launch()
```

## Configuration

### System Prompts
The client uses system prompts from the `prompts/` directory:

```python
# Use a specific system prompt
client = GradioClient(system_prompt_name="useful_assistant")
```

### Environment Variables
Make sure you have the following environment variables set:
- `OPENAI_API_KEY`: For GPT models
- `ANTHROPIC_API_KEY`: For Claude models

## Error Handling

The class includes robust error handling:

- API errors are caught and displayed to the user
- Network issues are handled gracefully
- Invalid model selections are prevented

## Extending the Class

To add new models or interface types:

1. **Add a new model client** in the `classes/` directory
2. **Extend the GradioClient** with new methods
3. **Create new interface types** using the existing patterns

Example of adding a new model:

```python
def stream_new_model(self, user_prompt: str) -> Generator[str, None, None]:
    # Implementation for new model
    pass

def create_new_model_interface(self) -> gr.Interface:
    # Interface for new model
    pass
```

## Example Usage

See `ui/gradio_client_example.py` for complete examples of all interface types.

## Dependencies

- `gradio`: For UI components
- `openai`: For GPT models
- `anthropic`: For Claude models
- `python-dotenv`: For environment variable management

## License

This class is part of the llm_exercises project and follows the same licensing terms.
