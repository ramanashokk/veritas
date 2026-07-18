from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class ConsensusStatus(StrEnum):
    """High-level outcome of evaluating evidence for a claim."""

    SUPPORTED = "SUPPORTED"
    CONTRADICTED = "CONTRADICTED"
    INCONCLUSIVE = "INCONCLUSIVE"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"


class ConsensusResult(BaseModel):
    """Deterministic synthesis of an evidence summary for a claim."""

    model_config = ConfigDict(frozen=True)

    claim_id: str
    status: ConsensusStatus
    confidence: float = Field(ge=0.0, le=1.0)
    reason: str
    support_score: float = Field(ge=0.0, le=1.0)
    contradict_score: float = Field(ge=0.0, le=1.0)
    neutral_score: float = Field(ge=0.0, le=1.0)
