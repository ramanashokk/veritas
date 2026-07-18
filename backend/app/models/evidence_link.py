from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class EvidenceRelationship(StrEnum):
    """The relationship between an observation and a claim."""

    SUPPORTS = "SUPPORTS"
    CONTRADICTS = "CONTRADICTS"
    NEUTRAL = "NEUTRAL"


class EvidenceLink(BaseModel):
    """Immutable representation of the relationship between an observation and a claim."""

    model_config = ConfigDict(frozen=True)

    observation_id: str
    claim_id: str
    relationship: EvidenceRelationship
