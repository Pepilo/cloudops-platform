from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_tasks():
    response = client.post("/tasks")

    assert response.status_code == 200
    assert response.json()["title"] == "Ma première tâche"
    assert response.json()["status"] == "todo"

def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["application"] == "TaskFlow API"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "service_healthy"