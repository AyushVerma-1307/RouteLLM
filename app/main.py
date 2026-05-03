from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.routes import router


app = FastAPI(
    title="RouteLLM API",
    description="Production-grade gateway for routing LLM requests",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
async def serve_frontend():
    return FileResponse("static/index.html")


@app.get("/health")
async def health_check():
    return {"status": "healthy"}