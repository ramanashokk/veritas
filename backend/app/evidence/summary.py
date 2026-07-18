from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class EvidenceSummary(BaseModel):
    """Temporary summary of evidence generated from a set of observations.

    Confidence is currently defined as support_count / total_count when there is
    at least one observation. This is a placeholder and will be refined later.
    """

    model_config = ConfigDict(frozen=True)

    claim_id: str
    support_count: int = Field(ge=0)
    contradict_count: int = Field(ge=0)
    neutral_count: int = Field(ge=0)
    confidence: float = Field(ge=0.0, le=1.0)
