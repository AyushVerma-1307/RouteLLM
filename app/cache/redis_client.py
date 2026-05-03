import redis
import hashlib
import json
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")


class RedisClient:
    def __init__(self):
        try:
            self.client = redis.from_url(REDIS_URL, decode_responses=True)
            self.client.ping()
        except redis.ConnectionError:
            self.client = None

    def is_available(self) -> bool:
        return self.client is not None

    def get(self, key: str) -> Optional[str]:
        if not self.is_available():
            return None
        return self.client.get(key)

    def set(self, key: str, value: str, ttl: int = 3600) -> bool:
        if not self.is_available():
            return False
        self.client.setex(key, ttl, value)
        return True

    def delete(self, key: str) -> bool:
        if not self.is_available():
            return False
        self.client.delete(key)
        return True


def generate_cache_key(prompt: str, provider: str) -> str:
    """Generate a unique cache key for a prompt + provider combination."""
    raw = f"{provider}:{prompt}"
    hashed = hashlib.sha256(raw.encode()).hexdigest()
    return f"llm_cache:{hashed}"


# Default instance
redis_client = RedisClient()