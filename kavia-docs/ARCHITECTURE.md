# PixelQuest Architecture & Backend Integration

This document outlines the architecture of the APIServer (Backend_FastAPI) and its integration strategy with the GameClient (Frontend_ReactJS).

---

## Overview

- **APIServer:** Lightweight FastAPI backend, reserved for features such as online leaderboards, multiplayer, and cloud saves. Initial version has health and root endpoints but is prepared for modular expansion.
- **GameClient:** All gameplay, state management, and UI are handled client-side in React. Integrates with backend only for optional online features.

---

## Implementation Structure

```mermaid
flowchart LR
    subgraph Frontend [GameClient (ReactJS)]
      F1["Game Logic & Rendering"]
      F2["State (zustand)"]
      F3["UI/Audio/Persistence"]
      F4["API Utilities (utils/api.ts)"]
      F1 --> F2
      F2 --> F3
      F3 --> F4
    end

    subgraph Backend [API Server (FastAPI)]
      B1["main.py (FastAPI Entrypoint)"]
      B2["endpoints/"]
      B3["models/ (future)"]
      B4["services/ (future)"]
      B1 --> B2
      B2 --> B3
      B2 --> B4
    end

    F4 --REST API Calls (future)--> B2
```

---

## Extensibility Points

- **Adding Endpoints:** Place new routes in `endpoints/`, organized by domain (e.g., `leaderboard.py`).
- **Defining Schemas:** Add new request/response types in `models/`.
- **Business Logic:** Implement in `services/` for separation of endpoint logic and core processing.

## Integration Approach

- **No dependency:** Initial frontend does not require backend; all features are optional.
- **CORS enabled:** FastAPI config allows requests from frontend for effortless local and deployed interoperation.
- **API versioning:** Prepared to add version tags/timestamped endpoints as features roll out.

---

## Separation of Concerns

- **Frontend:** All UI, input, animation, and persistence logic.
- **Backend:** Only backend-specific features—authentication, leaderboards, or other cloud capabilities (future).

---

## Folder Structure (Backend)

- `main.py` — FastAPI setup and router registration.
- `endpoints/` — All API routes (root, health, future features).
- `models/` — Pydantic data models (empty for now).
- `services/` — Service logic (empty for now).
- `requirements.txt` — Python dependencies.
- `README.md` — Project information.

---

### For more detail, refer to the Frontend documentation and codebase for context on integration and planned extensibility!
