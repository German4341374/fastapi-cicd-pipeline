import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.mark.integration
def test_health_endpoint() -> None:
    with TestClient(app) as client:
        response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


@pytest.mark.integration
def test_info_endpoint() -> None:
    with TestClient(app) as client:
        response = client.get("/api/info")
    assert response.status_code == 200
    assert response.json()["environment"] in {"development", "test", "production"}
