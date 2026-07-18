from __future__ import annotations

from app.search.results import SearchResult
from app.verification.result import VerificationResult, VerificationStatus

from app.api.dto.verify import ConsensusResponse, EvidenceResponse, VerificationResponse, VerifyResponse


class VerifyResponseMapper:
    """Maps internal verification artifacts into API DTOs."""

    def map(self, claim: str, verification: VerificationResult, evidence: list[SearchResult]) -> VerifyResponse:
        confidence_score = round(verification.confidence if verification.confidence > 0 else 0.35, 2)
        confidence_level = "high" if confidence_score >= 0.75 else "medium" if confidence_score >= 0.5 else "low"

        return VerifyResponse(
            claim=claim,
            verification=VerificationResponse(
                status=verification.status.value,
                confidence=verification.confidence,
            ),
            consensus=ConsensusResponse(classification=self._consensus_classification(verification.status)),
            evidence=[
                EvidenceResponse(
                    title=result.title,
                    source=result.source,
                    strength=self._strength_label(result),
                )
                for result in evidence
            ],
            question=claim,
            confidence_level=confidence_level,
            confidence_score=confidence_score,
        )

    def _consensus_classification(self, status: VerificationStatus) -> str:
        if status is VerificationStatus.VERIFIED:
            return "Strong Consensus"
        if status is VerificationStatus.LIKELY_TRUE:
            return "Moderate Consensus"
        if status is VerificationStatus.REFUTED:
            return "Strong Contradiction"
        if status is VerificationStatus.LIKELY_FALSE:
            return "Moderate Contradiction"
        if status is VerificationStatus.UNCERTAIN:
            return "Mixed Evidence"
        return "Insufficient Evidence"

    def _strength_label(self, result: SearchResult) -> str:
        if result.doi:
            return "HIGH"
        return "MEDIUM"
