from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Day 08 Protein Analyzer API"}


def test_protein_endpoint():
    response = client.get("/protein/TP53")

    assert response.status_code == 200
    data = response.json()

    assert "gene" in data
    assert "protein_id" in data
    assert "sequence" in data
    assert "composition" in data

def test_protein_stats():
    response = client.get("/protein/TP53/stats")

    assert response.status_code == 200
    data = response.json()

    assert "length" in data
    assert "gc_content" in data
    assert "composition" in data