from fastapi.testclient import TestClient

from pirate_translator.api import app

client = TestClient(app)


def test_health_ok():
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"
    assert "version" in body


def test_translate_endpoint():
    resp = client.post(
        "/translate",
        json={"text": "Olá amigo", "add_interjections": False},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["original"] == "Olá amigo"
    assert body["translated"] == "Ahoy marujo"


def test_translate_endpoint_with_interjections_seed():
    resp = client.post(
        "/translate",
        json={"text": "amigo", "add_interjections": True, "seed": 0},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert "marujo" in body["translated"].lower()


def test_terms_endpoint_returns_list():
    resp = client.get("/terms")
    assert resp.status_code == 200
    body = resp.json()
    assert isinstance(body["terms"], list)
    assert "amigo" in body["terms"]
