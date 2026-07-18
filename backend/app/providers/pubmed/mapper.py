from __future__ import annotations

from typing import Any

from app.search.results import SearchResult


class PubMedMapper:
    """Maps parsed PubMed records into Veritas SearchResult objects."""

    def map(self, records: list[dict[str, Any]]) -> list[SearchResult]:
        results: list[SearchResult] = []
        for record in records:
            title = record.get("title") or ""
            abstract = record.get("abstract")
            authors = record.get("authors") or []
            journal = record.get("journal")
            publication_year = record.get("publication_year")
            doi = record.get("doi")
            url = record.get("url")
            metadata = {
                "source_record_id": record.get("id"),
                "pubmed_id": record.get("id"),
            }
            results.append(
                SearchResult(
                    source="pubmed",
                    document_id=str(record.get("id") or title),
                    title=title,
                    abstract=abstract,
                    authors=[str(item) for item in authors if str(item)],
                    journal=journal,
                    publication_year=publication_year,
                    doi=doi,
                    url=url,
                    metadata=metadata,
                )
            )
        return results
