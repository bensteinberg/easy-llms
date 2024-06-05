# llama270b.py
from .aws import AWS

class Llama270b(AWS):
    name = "llama2_70b"
    model = "meta.llama2-70b-chat-v1"  # Override class variable

    def __init__(self, temperature=0.2, max_tokens=2048, **model_kwargs):
        super().__init__(**model_kwargs)

        self.model_kwargs = {
            "temperature": temperature,
            "max_gen_len": max_tokens,
            **model_kwargs
        }


        try:
            self.updateLLM()
        except Exception as e:
            print(f"Error updating LLM in {self.__class__.__name__}: {e}")

