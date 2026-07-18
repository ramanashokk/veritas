from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Claim(BaseModel):
    """Immutable representation of a proposition that can be evaluated with evidence."""

    model_config = ConfigDict(frozen=True)

    id: str
    text: str
    created_at: datetime
