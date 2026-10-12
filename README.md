# MovieBox API scaffold

This is a deployable FastAPI starter, not a finished MovieBox streaming API. MovieBox-TUI is a Rust terminal application; its features do not automatically become HTTP endpoints. Provider-backed search, details, source extraction, and playback must be implemented against a verified provider interface and used only where you have rights/authorization.

## Run locally

```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows:
# .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000/docs`.

## Railway

1. Push this folder to a GitHub repository.
2. In Railway, create a project and deploy that GitHub repository.
3. Railway detects `Dockerfile`; `railway.json` configures `/health`.
4. Open the generated public domain and test `/`, `/health`, and `/docs`.

## Current status

- `/` and `/health` are functional.
- Route shapes are present for search, movie/TV details, sources, formats, streams, anime, live TV and subtitles.
- Provider-dependent endpoints return an explicit not-configured response or placeholder. They do not invent movie data or stream URLs.
- Add a real provider adapter in `app/providers/` and register it in `app/providers/registry.py`.
- Restrict CORS to your frontend domain before production.
