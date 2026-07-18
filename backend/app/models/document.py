from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Document(BaseModel):
    """Immutable representation of a document retrieved from a source."""

    model_config = ConfigDict(frozen=True)

    id: str
    source_id: str
    title: str
    authors: list[str] = Field(default_factory=list)
    publication_date: str | None = None
    identifier: str | None = None
    abstract: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
