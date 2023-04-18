import os
import sys

from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == "green"
