from __future__ import annotations

from .exceptions import InvalidSearchQueryError, ProviderUnavailableError
from .interfaces import SearchProvider
from .query import SearchQuery
from .results import SearchResult


class SearchEngine:
    """Aggregates search results from multiple provider implementations."""

    def __init__(self, providers: list[SearchProvider] | None = None) -> None:
        self._providers = list(providers or [])

    def search(self, query: SearchQuery) -> list[SearchResult]:
        if not query.claim and not query.keywords and not query.authors and not query.journal:
            raise InvalidSearchQueryError("Search query must include at least one search term.")

        if not self._providers:
            return []

        merged_results: list[SearchResult] = []
        for provider in self._providers:
            try:
                if not provider.health_check():
                    raise ProviderUnavailableError(f"Provider {provider.provider_name()} is unavailable")
                provider_results = provider.search(query)
            except Exception as exc:
                if isinstance(exc, ProviderUnavailableError):
                    continue
                if isinstance(exc, InvalidSearchQueryError):
                    raise
                continue

            merged_results.extend(provider_results)

        return self._deduplicate(merged_results)

    def _deduplicate(self, results: list[SearchResult]) -> list[SearchResult]:
        seen: set[tuple[str, str]] = set()
        deduplicated: list[SearchResult] = []

        for result in results:
            if result.doi:
                key = ("doi", result.doi.lower())
            else:
                normalized_title = self._normalize_title(result.title)
                key = ("title", normalized_title)

            if key in seen:
                continue

            seen.add(key)
            deduplicated.append(result)

        return deduplicated

    def _normalize_title(self, title: str) -> str:
        return " ".join(title.lower().split())
