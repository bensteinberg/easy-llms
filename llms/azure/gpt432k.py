# azure/gpt432k.py
from .azure import AzureOpenAI

class AzureGPT432k(AzureOpenAI):
    name = "azure_gpt_4_32k"
    model = "gpt-4-32k"  # Override class variable

    def __init__(self, temperature=0.2, max_tokens=8192, **model_kwargs):
        super().__init__(**model_kwargs)
        self.temperature = temperature
        self.max_tokens = max_tokens
        try:
            self.updateLLM()
        except Exception as e:
            print(f"Error updating LLM in {self.__class__.__name__}: {e}")
