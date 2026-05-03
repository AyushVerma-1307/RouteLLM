import json
import logging
from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.services.ollama_service import get_response
from app.cache.redis_client import redis_client, generate_cache_key

logger = logging.getLogger(__name__)

router = APIRouter()

CACHE_TTL = 3600  # 1 hour


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """Process a chat request with Redis caching."""
    cache_key = generate_cache_key(request.prompt, request.provider)

    # Check cache first
    cached = redis_client.get(cache_key)
    if cached:
        logger.info(f"Cache hit for key: {cache_key[:16]}...")
        data = json.loads(cached)
        return ChatResponse(
            response=data["response"],
            provider=data["provider"]
        )

    logger.info(f"Cache miss, calling provider: {request.provider}")

    try:
        response_text = await get_response(request.prompt, request.provider)

        # Store in cache
        cache_data = json.dumps({
            "response": response_text,
            "provider": request.provider
        })
        redis_client.set(cache_key, cache_data, CACHE_TTL)

        return ChatResponse(
            response=response_text,
            provider=request.provider
        )
    except Exception as e:
        logger.error(f"Error calling provider: {e}")
        raise HTTPException(status_code=500, detail=str(e))