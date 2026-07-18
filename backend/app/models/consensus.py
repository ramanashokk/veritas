from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class ConsensusLabel(StrEnum):
    """High-level label summarizing a claim's evidence balance."""

    SUPPORTS = "SUPPORTS"
    CONTRADICTS = "CONTRADICTS"
    NEUTRAL = "NEUTRAL"


class Consensus(BaseModel):
    """Immutable representation of the overall evaluation of a claim."""

    model_config = ConfigDict(frozen=True)

    claim_id: str
    support_count: int = Field(ge=0)
    contradict_count: int = Field(ge=0)
    neutral_count: int = Field(ge=0)
    confidence: float = Field(ge=0.0, le=1.0)
    label: ConsensusLabel
