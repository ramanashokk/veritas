from app.consensus.result import ConsensusResult, ConsensusStatus
from app.verification.engine import VerificationEngine
from app.verification.result import VerificationStatus


def test_verified() -> None:
    engine = VerificationEngine()
    consensus_result = ConsensusResult(
        claim_id="claim-1",
        status=ConsensusStatus.SUPPORTED,
        confidence=0.95,
        reason="Evidence strongly supports the claim.",
        support_score=0.95,
        contradict_score=0.05,
        neutral_score=0.0,
    )

    result = engine.evaluate(consensus_result)

    assert result.status is VerificationStatus.VERIFIED
    assert result.explanation == "Available evidence strongly supports this claim."


def test_likely_true() -> None:
    engine = VerificationEngine()
    consensus_result = ConsensusResult(
        claim_id="claim-2",
        status=ConsensusStatus.SUPPORTED,
        confidence=0.89,
        reason="Evidence strongly supports the claim.",
        support_score=0.89,
        contradict_score=0.11,
        neutral_score=0.0,
    )

    result = engine.evaluate(consensus_result)

    assert result.status is VerificationStatus.LIKELY_TRUE
    assert result.explanation == "Available evidence generally supports this claim."


def test_refuted() -> None:
    engine = VerificationEngine()
    consensus_result = ConsensusResult(
        claim_id="claim-3",
        status=ConsensusStatus.CONTRADICTED,
        confidence=0.95,
        reason="Evidence strongly contradicts the claim.",
        support_score=0.05,
        contradict_score=0.95,
        neutral_score=0.0,
    )

    result = engine.evaluate(consensus_result)

    assert result.status is VerificationStatus.REFUTED
    assert result.explanation == "Available evidence strongly contradicts this claim."


def test_likely_false() -> None:
    engine = VerificationEngine()
    consensus_result = ConsensusResult(
        claim_id="claim-4",
        status=ConsensusStatus.CONTRADICTED,
        confidence=0.89,
        reason="Evidence strongly contradicts the claim.",
        support_score=0.11,
        contradict_score=0.89,
        neutral_score=0.0,
    )

    result = engine.evaluate(consensus_result)

    assert result.status is VerificationStatus.LIKELY_FALSE
    assert result.explanation == "Available evidence generally contradicts this claim."


def test_uncertain() -> None:
    engine = VerificationEngine()
    consensus_result = ConsensusResult(
        claim_id="claim-5",
        status=ConsensusStatus.INCONCLUSIVE,
        confidence=0.5,
        reason="Current evidence is mixed.",
        support_score=0.5,
        contradict_score=0.5,
        neutral_score=0.0,
    )

    result = engine.evaluate(consensus_result)

    assert result.status is VerificationStatus.UNCERTAIN
    assert result.explanation == "Current evidence is inconclusive."


def test_insufficient_evidence() -> None:
    engine = VerificationEngine()
    consensus_result = ConsensusResult(
        claim_id="claim-6",
        status=ConsensusStatus.INSUFFICIENT_EVIDENCE,
        confidence=0.0,
        reason="No evidence available.",
        support_score=0.0,
        contradict_score=0.0,
        neutral_score=1.0,
    )

    result = engine.evaluate(consensus_result)

    assert result.status is VerificationStatus.INSUFFICIENT_EVIDENCE
    assert result.explanation == "There is currently insufficient evidence to evaluate this claim."


def test_threshold_boundary_at_0_90() -> None:
    engine = VerificationEngine()
    consensus_result = ConsensusResult(
        claim_id="claim-7",
        status=ConsensusStatus.SUPPORTED,
        confidence=0.90,
        reason="Evidence strongly supports the claim.",
        support_score=0.90,
        contradict_score=0.10,
        neutral_score=0.0,
    )

    result = engine.evaluate(consensus_result)

    assert result.status is VerificationStatus.VERIFIED
