from __future__ import annotations

from pydantic import BaseModel, Field, model_validator


class VerifyRequest(BaseModel):
    """Incoming request for claim verification."""

    claim: str | None = Field(default=None, max_length=1000, description="Scientific claim to verify")
    question: str | None = Field(default=None, min_length=1, max_length=1000, description="Legacy question field")

    @model_validator(mode="after")
    def validate_input(self) -> "VerifyRequest":
        if self.claim is None and self.question is None:
            raise ValueError("Either claim or question must be provided.")
        return self


class VerificationResponse(BaseModel):
    """Machine-readable verification verdict."""

    status: str
    confidence: float


class ConsensusResponse(BaseModel):
    """Machine-readable consensus summary."""

    classification: str


class EvidenceResponse(BaseModel):
    """Machine-readable evidence summary entry."""

    title: str
    source: str
    strength: str


class VerifyResponse(BaseModel):
    """Structured API response for claim verification."""

    claim: str
    verification: VerificationResponse
    consensus: ConsensusResponse
    evidence: list[EvidenceResponse]
    question: str | None = None
    confidence_level: str | None = None
    confidence_score: float | None = None
