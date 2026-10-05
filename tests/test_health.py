from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_route():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to WeatherWise API"
    assert response.json()["docs"] == "/docs"


def test_health_route():
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "message": "WeatherWise API is running",
    }