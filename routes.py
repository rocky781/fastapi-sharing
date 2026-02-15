from fastapi import APIRouter, UploadFile, File
from models import UploadResponse
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    return UploadResponse(filename=file.filename, message="File uploaded successfully")

@router.get("/files")
async def list_files():
    files = os.listdir(UPLOAD_DIR)
    return {"files": files}
