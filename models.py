from pydantic import BaseModel

class FileInfo(BaseModel):
    filename: str
    size: int
    content_type: str

class UploadResponse(BaseModel):
    filename: str
    message: str
