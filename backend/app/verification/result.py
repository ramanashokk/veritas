from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class VerificationStatus(StrEnum):
    """High-level user-facing outcome for a claim."""

    VERIFIED = "VERIFIED"
    LIKELY_TRUE = "LIKELY_TRUE"
    UNCERTAIN = "UNCERTAIN"
    LIKELY_FALSE = "LIKELY_FALSE"
    REFUTED = "REFUTED"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


class VerificationResult(BaseModel):
    """Deterministic translation of consensus into a user-facing verdict."""

    model_config = ConfigDict(frozen=True)

    claim_id: str
    status: VerificationStatus
    confidence: float = Field(ge=0.0, le=1.0)
    explanation: str
    consensus_status: str
