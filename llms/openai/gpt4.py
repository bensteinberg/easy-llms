# gpt4.py
from .openai import OpenAI

class GPT4(OpenAI):
    name = "gpt_4"
    model = "gpt-4"  # Override class variable

    def __init__(self, temperature=0.2, max_tokens=8192, **model_kwargs):
        super().__init__(**model_kwargs)
        self.temperature = temperature
        self.max_tokens = max_tokens
        try:
            self.updateLLM()
        except Exception as e:
            print(f"Error updating LLM in {self.__class__.__name__}: {e}")

