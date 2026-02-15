"""
Tests module
"""
import pytest
from fastapi.testclient import TestClient

def test_root():
    from main import app
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    from main import app
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
