from __future__ import annotations

from abc import ABC, abstractmethod

from .query import SearchQuery
from .results import SearchResult


class SearchProvider(ABC):
    """Interface implemented by all research-source adapters."""

    @abstractmethod
    def search(self, query: SearchQuery) -> list[SearchResult]:
        """Return normalized search results for the provided query."""

    @abstractmethod
    def health_check(self) -> bool:
        """Return whether the provider is available for search."""

    @abstractmethod
    def provider_name(self) -> str:
        """Return the provider identifier used in normalized results."""
