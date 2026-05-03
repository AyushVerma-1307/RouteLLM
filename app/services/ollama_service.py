import ollama
from typing import Optional


class OllamaService:
    def __init__(self, model: str = "gemma4:31b-cloud", base_url: Optional[str] = None):
        self.model = model
        self.base_url = base_url

    async def complete(self, prompt: str) -> str:
        """Send a prompt to Ollama and get the response."""
        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response["message"]["content"]


# Default instance
ollama_service = OllamaService()


async def get_response(prompt: str, model: str = "minimax-m2.5:cloud") -> str:
    """Get a response from Ollama."""
    service = OllamaService(model=model)
    return await service.complete(prompt)