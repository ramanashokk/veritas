from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Observation(BaseModel):
    """Immutable representation of a factual observation extracted from a document."""

    model_config = ConfigDict(frozen=True)

    id: str
    document_id: str
    text: str
    confidence: float = Field(ge=0.0, le=1.0)
    metadata: dict[str, Any] = Field(default_factory=dict)
