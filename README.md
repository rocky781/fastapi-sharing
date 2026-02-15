# FastAPI Sharing

## API Documentation

### Endpoints

#### GET /
Returns a welcome message.

#### GET /health
Health check endpoint.

#### POST /upload
Upload a file to the server.

#### GET /files
List all uploaded files.

## Running the Application

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Testing

```bash
curl -X GET http://localhost:8000/
curl -X POST -F "file=@file.txt" http://localhost:8000/upload
```
