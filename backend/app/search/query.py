from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class SearchQuery(BaseModel):
    """Partial, provider-agnostic search request for research documents."""

    model_config = ConfigDict(frozen=True)

    claim: str | None = None
    keywords: list[str] = Field(default_factory=list)
    authors: list[str] = Field(default_factory=list)
    journal: str | None = None
    from_year: int | None = None
    to_year: int | None = None
    max_results: int = Field(default=10, ge=1)
    language: str | None = None
