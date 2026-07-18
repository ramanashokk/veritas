from app.models.source import Source, SourceStatus
from app.sources.registry import SourceRegistry


def test_registry_initializes_with_builtin_sources() -> None:
    registry = SourceRegistry()

    sources = registry.list_sources()
    source_ids = {source.id for source in sources}

    assert {"pubmed", "openalex", "crossref"}.issubset(source_ids)
    assert registry.get("pubmed").status is SourceStatus.ACTIVE


def test_registry_registers_and_toggles_sources() -> None:
    registry = SourceRegistry()
    source = Source(
        id="custom-source",
        name="Custom Source",
        description="A placeholder catalog entry.",
        organization="Example Org",
        homepage="https://example.org",
        status=SourceStatus.EXPERIMENTAL,
        supported_identifiers=["doi"],
        metadata={"kind": "demo"},
    )

    registry.register(source)

    assert registry.get("custom-source") == source
    assert registry.list_sources()[-1].id == "custom-source"

    registry.disable("custom-source")
    assert registry.get("custom-source").status is SourceStatus.DISABLED

    registry.enable("custom-source")
    assert registry.get("custom-source").status is SourceStatus.ACTIVE
