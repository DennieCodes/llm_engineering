from abc import ABC, abstractmethod

class BaseLLMClient(ABC):
    @abstractmethod
    def generate_content(self, user_prompt):
        """Generate content from the LLM given a user prompt."""
        pass

    @abstractmethod
    def get_model_name(self):
        """Return the name of the model used by the client."""
        pass
