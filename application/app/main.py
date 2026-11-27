from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db, engine, Base
from app import models
from app.models import Task

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/tasks")
def create_tasks(db: Session = Depends(get_db)):
    task = Task(
        title="Ma première tâche",
        description="Test de connexion PostgreSQL",
        status="todo"
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status
    }

@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()

    return tasks

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