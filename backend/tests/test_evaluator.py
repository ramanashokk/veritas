from uuid import uuid4

from app.engine.evaluator import compute_consensus, evaluate_claim


def test_supported_claim_returns_moderate_support() -> None:
    claim_id = str(uuid4())
    links = evaluate_claim("Coffee reduces cardiovascular mortality", claim_id)
    consensus = compute_consensus(claim_id, links)

    assert len(links) == 3
    assert consensus.summary == "Moderate support"
    assert consensus.supporting_count == 2
    assert consensus.contradicting_count == 1


def test_mixed_evidence_when_support_equals_contradiction() -> None:
    claim_id = str(uuid4())
    links = evaluate_claim("Saturated fat causes heart disease", claim_id)
    consensus = compute_consensus(claim_id, links)

    assert len(links) == 2
    assert consensus.summary == "Mixed evidence"
    assert consensus.supporting_count == 1
    assert consensus.contradicting_count == 1


def test_unknown_claim_returns_no_evidence() -> None:
    claim_id = str(uuid4())
    links = evaluate_claim("This claim is not in the prototype dataset", claim_id)
    consensus = compute_consensus(claim_id, links)

    assert links == []
    assert consensus.summary == "No evidence"
    assert consensus.supporting_count == 0
    assert consensus.contradicting_count == 0


def test_no_observations_returns_no_evidence() -> None:
    claim_id = str(uuid4())
    links = evaluate_claim("Vitamin E slows aging", claim_id)
    consensus = compute_consensus(claim_id, links)

    assert links == []
    assert consensus.summary == "No evidence"
    assert consensus.supporting_count == 0
    assert consensus.contradicting_count == 0


def test_all_supporting_returns_strong_support() -> None:
    claim_id = str(uuid4())
    links = evaluate_claim("Regular exercise reduces all-cause mortality", claim_id)
    consensus = compute_consensus(claim_id, links)

    assert len(links) == 2
    assert consensus.summary == "Strong support"
    assert consensus.supporting_count == 2
    assert consensus.contradicting_count == 0
