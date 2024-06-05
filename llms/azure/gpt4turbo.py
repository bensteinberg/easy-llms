# azure/gpt4turbo.py
from .azure import AzureOpenAI

class AzureGPT4Turbo(AzureOpenAI):
    name = "azure_gpt_4_turbo"
    model = "gpt-4-turbo"  # Override class variable

    def __init__(self, temperature=0.2, max_tokens=4096, **model_kwargs):
        super().__init__(**model_kwargs)
        self.temperature = temperature
        self.max_tokens = max_tokens
        try:
            self.updateLLM()
        except Exception as e:
            print(f"Error updating LLM in {self.__class__.__name__}: {e}")