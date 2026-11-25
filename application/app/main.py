from fastapi import FastAPI

app = FastAPI()

@app.post("/tasks")
def create_tasks():
    return {
        "title": "titleexample",
        "description": "descriptionexample",
        "status": "statusexample"
    }

@app.get("/tasks")
def get_tasks():
    return {
        "title": "titleexample",
        "description": "descriptionexample",
        "status": "statusexample"
    }

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