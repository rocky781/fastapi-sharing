from fastapi import FastAPI

app = FastAPI(title="FastAPI Sharing", description="File sharing API")

@app.get("/")
def read_root():
    return {"message": "FastAPI Sharing API", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
