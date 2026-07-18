from __future__ import annotations

from collections.abc import Iterable

from app.models.source import Source, SourceStatus


class SourceRegistry:
    """In-memory catalog of evidence sources available to Veritas.

    The registry is intentionally simple and replaceable. It stores source
    metadata only and does not perform any network, API, or persistence work.
    """

    def __init__(self) -> None:
        self._sources: dict[str, Source] = {}
        self._register_builtin_sources()

    def _register_builtin_sources(self) -> None:
        for source in self._builtin_sources():
            self.register(source)

    def _builtin_sources(self) -> Iterable[Source]:
        return [
            Source(
                id="pubmed",
                name="PubMed",
                description="Biomedical literature database maintained by NCBI.",
                organization="NCBI",
                homepage="https://pubmed.ncbi.nlm.nih.gov",
                status=SourceStatus.ACTIVE,
                supported_identifiers=["pmid", "doi"],
                metadata={"domain": "biomedical"},
            ),
            Source(
                id="openalex",
                name="OpenAlex",
                description="Open scholarly metadata catalog for research works.",
                organization="OpenAlex",
                homepage="https://openalex.org",
                status=SourceStatus.ACTIVE,
                supported_identifiers=["doi", "pmid", "wikidata"],
                metadata={"domain": "scholarly"},
            ),
            Source(
                id="crossref",
                name="Crossref",
                description="DOI registration and metadata service for scholarly works.",
                organization="Crossref",
                homepage="https://www.crossref.org",
                status=SourceStatus.ACTIVE,
                supported_identifiers=["doi"],
                metadata={"domain": "scholarly"},
            ),
        ]

    def register(self, source: Source) -> None:
        """Register or replace a source definition in the registry."""

        self._sources[source.id] = source

    def get(self, source_id: str) -> Source | None:
        """Return the registered source with the given identifier, if present."""

        return self._sources.get(source_id)

    def list_sources(self) -> list[Source]:
        """Return all known sources in registration order."""

        return list(self._sources.values())

    def enable(self, source_id: str) -> Source | None:
        """Enable a source by updating its status to ACTIVE."""

        source = self._sources.get(source_id)
        if source is None:
            return None

        updated_source = source.model_copy(update={"status": SourceStatus.ACTIVE})
        self._sources[source_id] = updated_source
        return updated_source

    def disable(self, source_id: str) -> Source | None:
        """Disable a source by updating its status to DISABLED."""

        source = self._sources.get(source_id)
        if source is None:
            return None

        updated_source = source.model_copy(update={"status": SourceStatus.DISABLED})
        self._sources[source_id] = updated_source
        return updated_source
