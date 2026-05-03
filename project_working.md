# RouteLLM - Working Guide

This file contains all commands and instructions needed to work on this project.

## Prerequisites

- Python 3.8+
- Redis (for caching and rate limiting)
- Ollama (for local LLM models)

## Setup Commands

### 1. Clone and Install Dependencies

```bash
cd E:/Code/LLM\ Project/llm-gateway
pip install -r requirements.txt
pip install ollama redis
```

### 2. Start Redis (Windows)

```bash
# Using Redis for Windows or WSL
redis-server
```

Or install Redis for Windows: https://github.com/tporadowski/redis/releases

### 3. Start Ollama

```bash
ollama serve
```

### 4. List Available Models

```bash
ollama list
```

### 5. Start the Server

```bash
cd E:/Code/LLM\ Project/llm-gateway
python -m uvicorn app.main:app --reload --port 8000
```

### 6. Access the UI

Open `http://localhost:8000` in your browser.

## API Commands

### Health Check

```bash
curl http://localhost:8000/health
```

### Chat Endpoint

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello!", "provider": "minimax-m2.5:cloud"}'
```

### Available Models

- `minimax-m2.5:cloud`
- `gemma4:31b-cloud`

## Git Commands

### Check Status

```bash
git status
```

### Commit and Push

```bash
git add -A
git commit -m "Your message"
git push origin main
```

### Pull Latest

```bash
git pull origin main
```

## Current Model in Use

**Model:** `gemma4:31b-cloud`

(This is the default model being used for AI responses)

## Project Status

- [x] Phase 1 Step 1: Basic FastAPI app with `/chat` endpoint
- [x] Phase 1 Step 2: Ollama provider integration
- [x] Chat UI with vanilla JS
- [ ] Phase 2: Redis caching (IN PROGRESS)
- [ ] Phase 3: Rate limiting
- [ ] Phase 4: Authentication
- [ ] Phase 5: Usage tracking

## File Structure

```
llm-gateway/
├── app/
│   ├── main.py              # FastAPI app
│   ├── api/routes.py        # /chat endpoint
│   ├── models/schemas.py    # Request/Response models
│   └── services/ollama_service.py  # Ollama integration
├── static/index.html        # Chat UI
├── requirements.txt
├── .env.example
└── README.md
```

## Troubleshooting

### Redis Connection Error
Make sure Redis is running: `redis-cli ping` should return `PONG`

### Model Not Found
Make sure Ollama is running and the model is pulled:
```bash
ollama list
```

### Port Already in Use
Kill existing process or use different port:
```bash
python -m uvicorn app.main:app --reload --port 8001
```