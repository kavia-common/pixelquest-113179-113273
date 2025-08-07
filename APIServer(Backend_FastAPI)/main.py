"""
PixelQuest API Server (Backend - FastAPI)

This is the entry point for the PixelQuest backend API server. The initial version provides only a root
index route and a health-check endpoint, with a modular structure for future extension (database,
services, new endpoints, etc). The app is fully documented with OpenAPI/Swagger support.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importing routers from endpoints package
from endpoints.root import router as root_router
from endpoints.health import router as health_router

# Metadata for future expansion
tags_metadata = [
    {
        "name": "Root",
        "description": "Root and API information routes."
    },
    {
        "name": "Health",
        "description": "Health-check and service status monitoring endpoints."
    },
    # Extend with more tags as new endpoint modules are added
]

app = FastAPI(
    title="PixelQuest API Server",
    description="Backend server for PixelQuest. Reserved for future features like leaderboards, multiplayer, cloud saves, etc. No persistent storage in the initial release.",
    version="0.1.0",
    openapi_tags=tags_metadata
)

# Enable CORS - adjust origins for production deployment if required
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins for better security
    allow_methods=["*"],
    allow_headers=["*"]
)

# Register routers (all API endpoints live in endpoints/)
app.include_router(root_router)
app.include_router(health_router)

# Placeholder - for extensions such as DB connection, middlewares, error handlers

if __name__ == "__main__":
    import uvicorn
    # PUBLIC_INTERFACE
    # To run: python main.py or use 'uvicorn main:app --reload' for development
    uvicorn.run(app, host="0.0.0.0", port=8000)
