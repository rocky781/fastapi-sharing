# FastAPI File Sharing

FastAPI application for file sharing with upload and list endpoints.

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Documentation

Visit http://localhost:8000/docs for interactive API docs.

## Endpoints

- GET / - Welcome message
- GET /health - Health check
- GET /info - App info
- POST /upload - Upload file
- GET /files - List files
