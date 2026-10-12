from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import health, search, movies, tv, anime, live_tv, sources, streams, subtitles

app = FastAPI(
    title="MovieBox API",
    description="A starter REST API scaffold for integrating compatible, lawful media providers.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set your frontend domain in production.
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(search.router)
app.include_router(movies.router)
app.include_router(tv.router)
app.include_router(anime.router)
app.include_router(live_tv.router)
app.include_router(sources.router)
app.include_router(streams.router)
app.include_router(subtitles.router)

@app.get("/")
def root():
    return {
        "name": "MovieBox API",
        "version": "0.1.0",
        "status": "running",
        "docs": "/docs",
        "note": "Provider-backed search and streaming are not configured yet."
    }
