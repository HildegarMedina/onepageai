import sys
import tiktoken
from openai import OpenAI
from config.config import COLOR_DANGER
from config.models_pricing import MODELS_PRICING

class ChatGPT:

    def __init__(self, console, model="gpt-3.5-turbo", max_tokens=2200):
        self.console = console
        self.model = model
        self.openai = OpenAI()
        self.max_tokens = max_tokens
        self.encoding = tiktoken.encoding_for_model(model)

    def calculate_cost(self, prompt):
        prompt_length = len(self.encoding.encode(prompt))
        response_length = self.max_tokens
        input_price = (prompt_length * MODELS_PRICING[self.model]['input']) / 1000
        output_price = (response_length * MODELS_PRICING[self.model]['output']) / 1000
        return input_price + output_price

    def completion(self, prompt):
        try:
            response = self.openai.chat.completions.create(
                model=self.model,
                max_tokens=self.max_tokens,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            message =  response.choices[0].message.content
            return message
        except Exception as e:
            self.console.print(f"\n[{COLOR_DANGER}]Error: {e}\n")
            sys.exit(1)
