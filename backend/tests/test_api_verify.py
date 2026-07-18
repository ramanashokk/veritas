def test_verify_endpoint_returns_structured_response(client) -> None:
    response = client.post(
        "/api/v1/verify",
        json={"claim": "COVID-19 vaccines reduce hospitalization."},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["claim"] == "COVID-19 vaccines reduce hospitalization."
    assert payload["verification"]["status"] in {"VERIFIED", "LIKELY_TRUE", "UNCERTAIN", "LIKELY_FALSE", "REFUTED", "INSUFFICIENT_EVIDENCE"}
    assert payload["consensus"]["classification"]
    assert isinstance(payload["evidence"], list)


def test_verify_endpoint_rejects_blank_claim(client) -> None:
    response = client.post("/api/v1/verify", json={"claim": "   "})

    assert response.status_code == 400
    payload = response.json()
    assert payload["error"] == "Validation Error"


def test_verify_endpoint_returns_not_found_when_no_evidence(client) -> None:
    response = client.post("/api/v1/verify", json={"claim": "quantum unicorn healing"})

    assert response.status_code == 404
    payload = response.json()
    assert payload["error"] == "No Evidence Found"


def test_verify_endpoint_rejects_invalid_json(client) -> None:
    response = client.post("/api/v1/verify", data="{not valid json", headers={"content-type": "application/json"})

    assert response.status_code == 400
