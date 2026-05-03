# RouteLLM

A production-grade LLM API Gateway that routes requests to multiple LLM providers with caching, rate limiting, and usage tracking.

## Problem It Solves

Building AI-powered applications often requires:
- **Managing multiple LLM providers** (OpenAI, Anthropic, Ollama, etc.)
- **Handling API costs** through intelligent caching
- **Rate limiting** to prevent abuse
- **Usage tracking** per user or team
- **Failover** when providers go down

RouteLLM solves these by providing a unified API gateway that abstracts away provider differences and adds enterprise features on top.

## Features

- **Multi-Provider Support** - Route requests to OpenAI, Anthropic, Ollama, or any LLM provider
- **Redis Caching** - Cache responses to reduce API costs and improve latency
- **Rate Limiting** - Per-user rate limits to prevent abuse
- **Usage Tracking** - Track token usage and costs per user
- **Failover** - Automatic fallback when a provider fails
- **Simple API** - Single endpoint for all LLM interactions

## Tech Stack

- **Backend**: FastAPI (Python)
- **Cache & Rate Limiting**: Redis
- **Database**: PostgreSQL (for usage tracking)
- **LLM Providers**: OpenAI, Anthropic, Ollama
- **Frontend**: Vanilla JS (lightweight chat UI)

## Quick Start

### 1. Clone and Install

```bash
git clone https://github.com/AyushVerma-1307/RouteLLM.git
cd RouteLLM
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your API keys
```

### 3. Run the Server

```bash
python -m uvicorn app.main:app --reload --port 8000
```

### 4. Open the UI

Navigate to `http://localhost:8000` in your browser.

## API Usage

### Chat Endpoint

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello!", "provider": "minimax-m2.5:cloud"}'
```

**Request:**
```json
{
  "prompt": "Your message here",
  "provider": "ollama model name (optional, defaults to minimax-m2.5:cloud)"
}
```

**Response:**
```json
{
  "response": "AI response here",
  "provider": "minimax-m2.5:cloud"
}
```

### Health Check

```bash
curl http://localhost:8000/health
```

## Project Structure

```
llm-gateway/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── api/
│   │   └── routes.py        # API endpoints
│   ├── models/
│   │   └── schemas.py       # Pydantic models
│   ├── services/
│   │   └── ollama_service.py # LLM provider integration
│   ├── cache/
│   │   └── redis_client.py  # Redis caching
│   └── rate_limit/
│       └── limiter.py       # Rate limiting
├── static/
│   └── index.html           # Chat UI
├── requirements.txt
└── .env.example
```

## Currently Supported Models

- **Ollama**: `minimax-m2.5:cloud`, `minimax-m2.7:cloud`, `gemma4:31b-cloud`, `llama3.2`
- **OpenAI**: gpt-4, gpt-3.5-turbo (coming soon)
- **Anthropic**: Claude-3 (coming soon)

## Roadmap

- [x] Basic `/chat` endpoint with Ollama
- [x] Chat UI
- [x] Redis caching layer
- [ ] Rate limiting per user
- [ ] API key authentication
- [ ] PostgreSQL for usage tracking
- [ ] OpenAI provider integration
- [ ] Anthropic provider integration
- [ ] Streaming responses
- [ ] Failover logic

## License

MIT