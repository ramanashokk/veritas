from __future__ import annotations

from app.search.exceptions import ProviderUnavailableError
from app.search.query import SearchQuery
from app.search.results import SearchResult

from .client import PubMedClient
from .mapper import PubMedMapper
from .parser import PubMedParser


class PubMedProvider:
    """PubMed implementation of the search provider interface."""

    def __init__(self, client: PubMedClient | None = None, parser: PubMedParser | None = None, mapper: PubMedMapper | None = None) -> None:
        self._client = client or PubMedClient()
        self._parser = parser or PubMedParser()
        self._mapper = mapper or PubMedMapper()

    def search(self, query: SearchQuery) -> list[SearchResult]:
        try:
            query_text = self._build_query(query)
            raw_response = self._client.search(
                query=query_text,
                max_results=query.max_results,
                from_year=query.from_year,
                to_year=query.to_year,
            )
            parsed_records = self._parser.parse({"results": raw_response})
            return self._mapper.map(parsed_records)
        except ProviderUnavailableError:
            raise
        except Exception as exc:  # pragma: no cover - defensive for tests
            raise ProviderUnavailableError(f"PubMed provider failed: {exc}") from exc

    def health_check(self) -> bool:
        return True

    def provider_name(self) -> str:
        return "pubmed"

    def _build_query(self, query: SearchQuery) -> str:
        parts: list[str] = []
        if query.claim:
            parts.append(query.claim)
        if query.keywords:
            parts.extend(query.keywords)
        if not parts:
            return ""
        return " ".join(parts)
