import os

class Config:
    APP_NAME = "FastAPI Sharing"
    VERSION = "1.0.0"
    UPLOAD_DIR = "uploads"
    MAX_FILE_SIZE = 100 * 1024 * 1024
    
    @staticmethod
    def init():
        os.makedirs(Config.UPLOAD_DIR, exist_ok=True)
