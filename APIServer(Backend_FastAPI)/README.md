# PixelQuest API Server (Backend - FastAPI)

This is the backend API server for PixelQuest, built with **FastAPI**.  
**Purpose:**  
- Intended for future extensibility—online leaderboards, multiplayer, cloud save, etc.
- Not required for single-player game logic; no persistent storage in the initial version.

## Structure

- `main.py` — FastAPI app entry point, sets up routing and OpenAPI docs
- `endpoints/` — All API routes, organized per feature/module
    - `root.py` — Root (`/`) API home
    - `health.py` — Health-check (`/health`)
- `models/` — Pydantic schemas (add in future)
- `services/` — Business logic/services (add in future)

## Running Locally

```
pip install -r requirements.txt
uvicorn main:app --reload
```

Navigate to [http://localhost:8000/docs](http://localhost:8000/docs) for the API docs (Swagger UI).

## Extending

- Add new endpoints in `endpoints/`
- Add request/response schemas in `models/`
- Implement business logic in `services/`
- Future: Integrate database, authentication, etc.

## Project Status

This is a placeholder backend. No user/game data or gameplay logic is handled server-side in the initial release.
