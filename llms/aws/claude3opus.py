# claude3opus.py
from .aws import AWS

class Claude3Opus(AWS):
    name = "claude_3_opus"
    model = "anthropic.claude-3-opus-20240229-v1:0"  # Override class variable

    def __init__(self, temperature=0.2, max_tokens=4096, **model_kwargs):
        super().__init__(**model_kwargs)

        self.model_kwargs = {
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stop_sequences": ["\n\nHuman"],
            **model_kwargs
        }


        try:
            self.updateLLM()
        except Exception as e:
            print(f"Error updating LLM in {self.__class__.__name__}: {e}")
