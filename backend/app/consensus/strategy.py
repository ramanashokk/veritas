from __future__ import annotations

from abc import ABC, abstractmethod

from app.evidence.summary import EvidenceSummary

from .result import ConsensusResult, ConsensusStatus


class ConsensusStrategy(ABC):
    """Strategy interface for turning evidence summaries into consensus results."""

    @abstractmethod
    def evaluate(self, evidence_summary: EvidenceSummary) -> ConsensusResult:
        """Return a consensus result for the provided evidence summary."""


class SimpleConsensusStrategy(ConsensusStrategy):
    """Version 1 deterministic consensus strategy.

    This strategy intentionally uses only support and contradict counts and does
    not incorporate evidence quality, source reliability, recency, or other
    scientific weighting factors yet.
    """

    def evaluate(self, evidence_summary: EvidenceSummary) -> ConsensusResult:
        total_supporting_and_contradicting = (
            evidence_summary.support_count + evidence_summary.contradict_count
        )

        if total_supporting_and_contradicting == 0:
            return ConsensusResult(
                claim_id=evidence_summary.claim_id,
                status=ConsensusStatus.INSUFFICIENT_EVIDENCE,
                confidence=0.0,
                reason="No evidence available.",
                support_score=0.0,
                contradict_score=0.0,
                neutral_score=1.0,
            )

        support_ratio = evidence_summary.support_count / total_supporting_and_contradicting
        contradict_ratio = evidence_summary.contradict_count / total_supporting_and_contradicting
        neutral_ratio = evidence_summary.neutral_count / max(1, total_supporting_and_contradicting)

        if support_ratio >= 0.70:
            return ConsensusResult(
                claim_id=evidence_summary.claim_id,
                status=ConsensusStatus.SUPPORTED,
                confidence=support_ratio,
                reason="Evidence strongly supports the claim.",
                support_score=support_ratio,
                contradict_score=contradict_ratio,
                neutral_score=neutral_ratio,
            )

        if support_ratio <= 0.30:
            return ConsensusResult(
                claim_id=evidence_summary.claim_id,
                status=ConsensusStatus.CONTRADICTED,
                confidence=1 - support_ratio,
                reason="Evidence strongly contradicts the claim.",
                support_score=support_ratio,
                contradict_score=contradict_ratio,
                neutral_score=neutral_ratio,
            )

        confidence = round(abs(0.5 - support_ratio) * 2, 10)
        if confidence < 0.0:
            confidence = 0.0
        if confidence > 1.0:
            confidence = 1.0

        return ConsensusResult(
            claim_id=evidence_summary.claim_id,
            status=ConsensusStatus.INCONCLUSIVE,
            confidence=confidence,
            reason="Current evidence is mixed.",
            support_score=support_ratio,
            contradict_score=contradict_ratio,
            neutral_score=neutral_ratio,
        )
