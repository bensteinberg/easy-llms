# mistrallarge.py
from .aws import AWS

class MistralLarge(AWS):
    name = "mistral_large"
    model = "mistral.mistral-large-2402-v1:0"  # Override class variable

    def __init__(self, temperature=0.2, max_tokens=4096, **model_kwargs):
        super().__init__(**model_kwargs)

        self.model_kwargs = {
            "temperature": temperature,
            "max_tokens": max_tokens,
            **model_kwargs
        }


        try:
            self.updateLLM()
        except Exception as e:
            print(f"Error updating LLM in {self.__class__.__name__}: {e}")
