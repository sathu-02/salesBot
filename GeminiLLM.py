from pandasai.llm.base import LLM
import google.generativeai as genai

class GeminiLLM(LLM):
    def __init__(self, api_key: str, model: str = "gemini-2.5-pro", system_prompt: str = None):
        self.api_key = api_key
        self.model = model
        self.system_prompt = system_prompt or ""
        genai.configure(api_key=self.api_key)
        self.gemini = genai.GenerativeModel(model)

    def call(self, prompt: str, *args, **kwargs) -> str:
    # Safely convert any input to string first
        prompt_str = str(prompt).strip()
        full_prompt = f"{self.system_prompt.strip()}\n\n{prompt_str}"
        response = self.gemini.generate_content(full_prompt)
        return response.text.strip()



    def type(self) -> str:
        return "gemini"  # Add this method to fix the error
