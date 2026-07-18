from app.search.engine import SearchEngine
from app.search.exceptions import InvalidSearchQueryError
from app.search.interfaces import SearchProvider
from app.search.query import SearchQuery
from app.search.results import SearchResult


class StubProvider(SearchProvider):
    def __init__(self, name: str, results: list[SearchResult] | None = None, healthy: bool = True) -> None:
        self._name = name
        self._results = results or []
        self._healthy = healthy

    def search(self, query: SearchQuery) -> list[SearchResult]:
        return self._results

    def health_check(self) -> bool:
        return self._healthy

    def provider_name(self) -> str:
        return self._name


def test_empty_provider_list_returns_empty_results() -> None:
    engine = SearchEngine([])

    results = engine.search(SearchQuery(claim="coffee reduces heart disease", max_results=5))

    assert results == []


def test_single_provider_returns_results() -> None:
    provider = StubProvider(
        "demo",
        [SearchResult(source="demo", document_id="doc-1", title="Coffee and heart disease", doi="10.1234/demo")],
    )
    engine = SearchEngine([provider])

    results = engine.search(SearchQuery(claim="coffee reduces heart disease", max_results=5))

    assert len(results) == 1
    assert results[0].document_id == "doc-1"


def test_multiple_providers_aggregate_results() -> None:
    provider_a = StubProvider(
        "a",
        [SearchResult(source="a", document_id="doc-1", title="Coffee and heart disease", doi="10.1111/a")],
    )
    provider_b = StubProvider(
        "b",
        [SearchResult(source="b", document_id="doc-2", title="Coffee and mortality", doi="10.2222/b")],
    )
    engine = SearchEngine([provider_a, provider_b])

    results = engine.search(SearchQuery(claim="coffee reduces heart disease", max_results=5))

    assert len(results) == 2


def test_duplicate_doi_removal() -> None:
    provider_a = StubProvider(
        "a",
        [SearchResult(source="a", document_id="doc-1", title="Coffee and heart disease", doi="10.1234/shared")],
    )
    provider_b = StubProvider(
        "b",
        [SearchResult(source="b", document_id="doc-2", title="Coffee and heart disease", doi="10.1234/shared")],
    )
    engine = SearchEngine([provider_a, provider_b])

    results = engine.search(SearchQuery(claim="coffee and heart disease", max_results=5))

    assert len(results) == 1


def test_duplicate_title_removal() -> None:
    provider_a = StubProvider(
        "a",
        [SearchResult(source="a", document_id="doc-1", title="Coffee and heart disease")],
    )
    provider_b = StubProvider(
        "b",
        [SearchResult(source="b", document_id="doc-2", title="Coffee   and   heart disease")],
    )
    engine = SearchEngine([provider_a, provider_b])

    results = engine.search(SearchQuery(claim="coffee and heart disease", max_results=5))

    assert len(results) == 1


def test_provider_failure_isolation() -> None:
    failing_provider = StubProvider("broken", healthy=False)
    working_provider = StubProvider(
        "working",
        [SearchResult(source="working", document_id="doc-1", title="Coffee and heart disease", doi="10.1234/ok")],
    )
    engine = SearchEngine([failing_provider, working_provider])

    results = engine.search(SearchQuery(claim="coffee and heart disease", max_results=5))

    assert len(results) == 1
    assert results[0].source == "working"


def test_invalid_query_raises_error() -> None:
    engine = SearchEngine([])

    try:
        engine.search(SearchQuery())
    except InvalidSearchQueryError:
        assert True
    else:
        raise AssertionError("Expected InvalidSearchQueryError")
