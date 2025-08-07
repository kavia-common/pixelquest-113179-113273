"""
Endpoints related to root ('/') and API home for PixelQuest API Server.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

# PUBLIC_INTERFACE
@router.get("/", summary="API Home", tags=["Root"])
async def api_home():
    """
    Root endpoint for PixelQuest API server.

    Returns a welcome message and brief documentation.
    For full API details, visit the /docs endpoint for Swagger UI.

    Returns:
        JSON containing project name, status, and usage notes.
    """
    return JSONResponse(
        content={
            "project": "PixelQuest API Server",
            "version": "0.1.0",
            "status": "OK",
            "description": (
                "API backend for PixelQuest game. "
                "This server is currently a placeholder—future features like leaderboards and online saves will be added. "
                "Access /health for health checks or /docs for interactive API documentation."
            ),
            "documentation_url": "/docs"
        }
    )
