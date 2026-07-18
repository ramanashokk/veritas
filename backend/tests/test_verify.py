def test_verify_returns_mocked_response(client) -> None:
    response = client.post(
        "/api/v1/verify",
        json={"question": "Does caffeine improve cognitive performance?"},
    )

    assert response.status_code == 200
    body = response.json()

    assert body["question"] == "Does caffeine improve cognitive performance?"
    assert body["claim"] == body["question"]
    assert body["confidence_level"] == "low"
    assert body["confidence_score"] == 0.35
    assert len(body["evidence"]) == 2
    assert body["evidence"][0]["title"].startswith("[Mock]")


def test_verify_rejects_empty_question(client) -> None:
    response = client.post("/api/v1/verify", json={"question": ""})

    assert response.status_code == 422
