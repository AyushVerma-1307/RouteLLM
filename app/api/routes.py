from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.services.ollama_service import get_response


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """Process a chat request and return a response from Ollama."""
    try:
        response_text = await get_response(request.prompt, request.provider)
        return ChatResponse(
            response=response_text,
            provider=request.provider
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))