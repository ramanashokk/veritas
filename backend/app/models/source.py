from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Source(BaseModel):
    """Immutable representation of where information originates."""

    model_config = ConfigDict(frozen=True)

    id: str
    name: str
    type: str
    url: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
