from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_health_check():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_generate_testcases_endpoint():
    payload = {
        "requirement_text": (
            "As a user, I want to add items to my shopping cart "
            "so that I can buy multiple products in one order."
        ),
        "num_cases": 3,
        "style": "plain",
    }

    resp = client.post("/generate-testcases", json=payload)
    assert resp.status_code == 200

    data = resp.json()
    assert "test_cases" in data
    assert len(data["test_cases"]) >= 1

    first = data["test_cases"][0]
    assert "title" in first
    assert "steps" in first
    assert "expected_result" in first

