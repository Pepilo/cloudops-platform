from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "application": "TaskFlow API",
        "message": "Welcome to this demo project!"
    }

@app.get("/health")
def health():
    return {
        "status": "service_healthy"
    }