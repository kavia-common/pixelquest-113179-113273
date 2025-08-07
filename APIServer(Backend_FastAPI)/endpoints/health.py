"""
Endpoints for health and readiness checks for PixelQuest API Server.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/health")


# PUBLIC_INTERFACE
@router.get("/", summary="Health Check", description="Basic health check to confirm API is running.", tags=["Health"])
async def health_check():
    """
    Returns service status—useful for uptime/readiness monitoring.

    Returns:
        JSON object with 'status' (always "healthy" in this initial version).
    """
    return JSONResponse(content={"status": "healthy"})
