from fastapi import APIRouter

router = APIRouter()

@router.get("/info")
async def app_info():
    return {
        "name": "FastAPI Sharing",
        "version": "1.0.0",
        "description": "File sharing API built with FastAPI"
    }
