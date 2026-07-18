from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class SourceStatus(StrEnum):
    """Catalog status for a source in Veritas."""

    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    EXPERIMENTAL = "EXPERIMENTAL"


class Source(BaseModel):
    """Immutable representation of where information originates."""

    model_config = ConfigDict(frozen=True)

    id: str
    name: str
    description: str | None = None
    organization: str | None = None
    homepage: str | None = None
    status: SourceStatus = SourceStatus.ACTIVE
    supported_identifiers: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
