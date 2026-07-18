from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class SearchResult(BaseModel):
    """Normalized document representation returned by any search provider."""

    model_config = ConfigDict(frozen=True)

    source: str
    document_id: str
    title: str
    abstract: str | None = None
    authors: list[str] = Field(default_factory=list)
    journal: str | None = None
    publication_year: int | None = None
    doi: str | None = None
    url: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
