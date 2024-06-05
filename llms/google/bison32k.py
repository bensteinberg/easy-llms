# bison32k.py
from .google import Google

class Bison32k(Google):
    name = "bison-32k"
    model = "chat-bison-32k"  # Override class variable

    def __init__(self, temperature=0.2, max_tokens=8192, **model_kwargs):
        super().__init__(**model_kwargs)

        self.temperature=temperature
        self.max_tokens=max_tokens

        try:
            self.updateLLM()
        except Exception as e:
            print(f"Error updating LLM in {self.__class__.__name__}: {e}")
