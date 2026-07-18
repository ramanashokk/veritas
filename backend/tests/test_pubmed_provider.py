from unittest.mock import Mock

import pytest

from app.providers.pubmed.client import PubMedClient
from app.providers.pubmed.mapper import PubMedMapper
from app.providers.pubmed.parser import PubMedParser
from app.providers.pubmed.provider import PubMedProvider
from app.search.exceptions import ProviderUnavailableError
from app.search.query import SearchQuery


def test_query_construction_uses_claim_and_keywords() -> None:
    provider = PubMedProvider()

    query = SearchQuery(claim="coffee reduces heart disease", keywords=["cardiovascular", "risk"], max_results=3)

    assert provider._build_query(query) == "coffee reduces heart disease cardiovascular risk"


def test_parser_returns_structured_records() -> None:
    parser = PubMedParser()

    parsed = parser.parse({"results": [{"id": "123", "title": "Study"}]})

    assert parsed[0]["id"] == "123"


def test_mapper_creates_search_results() -> None:
    mapper = PubMedMapper()

    results = mapper.map([
        {
            "id": "123",
            "title": "Coffee and heart disease",
            "abstract": "A summary",
            "authors": ["Ada Lovelace"],
            "journal": "Nature",
            "publication_year": 2024,
            "doi": "10.1234/example",
            "url": "https://example.org",
        }
    ])

    assert results[0].source == "pubmed"
    assert results[0].doi == "10.1234/example"


def test_provider_integration_uses_client_parser_and_mapper(monkeypatch: pytest.MonkeyPatch) -> None:
    client = Mock()
    client.search.return_value = [{"id": "123", "title": "Coffee and heart disease"}]
    parser = PubMedParser()
    mapper = PubMedMapper()

    provider = PubMedProvider(client=client, parser=parser, mapper=mapper)
    results = provider.search(SearchQuery(claim="coffee", max_results=1))

    assert len(results) == 1
    assert results[0].document_id == "123"


def test_provider_wraps_network_failures() -> None:
    client = Mock()
    client.search.side_effect = ProviderUnavailableError("boom")
    provider = PubMedProvider(client=client)

    with pytest.raises(ProviderUnavailableError):
        provider.search(SearchQuery(claim="coffee", max_results=1))


def test_empty_response_returns_empty_results() -> None:
    provider = PubMedProvider(client=Mock(search=Mock(return_value=[])))

    results = provider.search(SearchQuery(claim="coffee", max_results=1))

    assert results == []
