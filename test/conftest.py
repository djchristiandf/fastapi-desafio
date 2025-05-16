import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_headers():
    # Implemente um mock de token JWT se necessário
    return {"Authorization": "Bearer mock-token"}