from __future__ import annotations

from abc import ABC, abstractmethod

from app.consensus.result import ConsensusResult, ConsensusStatus


class VerificationRule(ABC):
    """Strategy interface for converting consensus results to user-facing verdicts."""

    @abstractmethod
    def evaluate(self, consensus_result: ConsensusResult) -> "VerificationResult":
        """Return a verification result for the provided consensus result."""


class SimpleVerificationRule(VerificationRule):
    """Version 1 deterministic mapping from consensus to user-facing verdicts."""

    def evaluate(self, consensus_result: ConsensusResult) -> "VerificationResult":
        from .result import VerificationResult, VerificationStatus

        if consensus_result.status is ConsensusStatus.SUPPORTED:
            if consensus_result.confidence >= 0.90:
                return VerificationResult(
                    claim_id=consensus_result.claim_id,
                    status=VerificationStatus.VERIFIED,
                    confidence=consensus_result.confidence,
                    explanation="Available evidence strongly supports this claim.",
                    consensus_status=consensus_result.status.value,
                )
            return VerificationResult(
                claim_id=consensus_result.claim_id,
                status=VerificationStatus.LIKELY_TRUE,
                confidence=consensus_result.confidence,
                explanation="Available evidence generally supports this claim.",
                consensus_status=consensus_result.status.value,
            )

        if consensus_result.status is ConsensusStatus.CONTRADICTED:
            if consensus_result.confidence >= 0.90:
                return VerificationResult(
                    claim_id=consensus_result.claim_id,
                    status=VerificationStatus.REFUTED,
                    confidence=consensus_result.confidence,
                    explanation="Available evidence strongly contradicts this claim.",
                    consensus_status=consensus_result.status.value,
                )
            return VerificationResult(
                claim_id=consensus_result.claim_id,
                status=VerificationStatus.LIKELY_FALSE,
                confidence=consensus_result.confidence,
                explanation="Available evidence generally contradicts this claim.",
                consensus_status=consensus_result.status.value,
            )

        if consensus_result.status is ConsensusStatus.INCONCLUSIVE:
            return VerificationResult(
                claim_id=consensus_result.claim_id,
                status=VerificationStatus.UNCERTAIN,
                confidence=consensus_result.confidence,
                explanation="Current evidence is inconclusive.",
                consensus_status=consensus_result.status.value,
            )

        return VerificationResult(
            claim_id=consensus_result.claim_id,
            status=VerificationStatus.INSUFFICIENT_EVIDENCE,
            confidence=consensus_result.confidence,
            explanation="There is currently insufficient evidence to evaluate this claim.",
            consensus_status=consensus_result.status.value,
        )
