from app.consensus.engine import ConsensusEngine
from app.consensus.result import ConsensusStatus
from app.evidence.summary import EvidenceSummary


def test_no_evidence() -> None:
    engine = ConsensusEngine()
    evidence_summary = EvidenceSummary(claim_id="claim-1", support_count=0, contradict_count=0, neutral_count=0, confidence=0.0)

    result = engine.evaluate(evidence_summary)

    assert result.status is ConsensusStatus.INSUFFICIENT_EVIDENCE
    assert result.confidence == 0.0
    assert result.reason == "No evidence available."


def test_strong_support() -> None:
    engine = ConsensusEngine()
    evidence_summary = EvidenceSummary(claim_id="claim-2", support_count=7, contradict_count=1, neutral_count=2, confidence=0.7)

    result = engine.evaluate(evidence_summary)

    assert result.status is ConsensusStatus.SUPPORTED
    assert result.confidence == 0.875
    assert result.reason == "Evidence strongly supports the claim."


def test_strong_contradiction() -> None:
    engine = ConsensusEngine()
    evidence_summary = EvidenceSummary(claim_id="claim-3", support_count=1, contradict_count=7, neutral_count=2, confidence=0.1)

    result = engine.evaluate(evidence_summary)

    assert result.status is ConsensusStatus.CONTRADICTED
    assert result.confidence == 0.875
    assert result.reason == "Evidence strongly contradicts the claim."


def test_mixed_evidence() -> None:
    engine = ConsensusEngine()
    evidence_summary = EvidenceSummary(claim_id="claim-4", support_count=2, contradict_count=2, neutral_count=3, confidence=0.5)

    result = engine.evaluate(evidence_summary)

    assert result.status is ConsensusStatus.INCONCLUSIVE
    assert result.confidence == 0.0
    assert result.reason == "Current evidence is mixed."


def test_borderline_values() -> None:
    engine = ConsensusEngine()
    evidence_summary = EvidenceSummary(claim_id="claim-5", support_count=3, contradict_count=2, neutral_count=1, confidence=0.6)

    result = engine.evaluate(evidence_summary)

    assert result.status is ConsensusStatus.INCONCLUSIVE
    assert result.confidence == 0.2
    assert result.reason == "Current evidence is mixed."
