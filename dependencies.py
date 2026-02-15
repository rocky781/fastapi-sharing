"""
Dependencies module
"""
from fastapi import Depends, HTTPException
from typing import Optional

async def get_current_user(token: Optional[str] = None):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {"user": "example"}

async def verify_api_key(api_key: Optional[str] = None):
    if not api_key:
        raise HTTPException(status_code=403, detail="API key required")
    return True
