from pydantic import BaseModel


class ChatRequest(BaseModel):
    prompt: str
    provider: str = "minimax-m2.5:cloud"


class ChatResponse(BaseModel):
    response: str
    provider: str