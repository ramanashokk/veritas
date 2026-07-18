from __future__ import annotations

import json
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from app.search.exceptions import ProviderUnavailableError

PUBMED_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
PUBMED_SEARCH_ENDPOINT = f"{PUBMED_BASE_URL}/esearch.fcgi"
PUBMED_SUMMARY_ENDPOINT = f"{PUBMED_BASE_URL}/esummary.fcgi"
PUBMED_FETCH_ENDPOINT = f"{PUBMED_BASE_URL}/efetch.fcgi"


class PubMedClient:
    """Low-level HTTP client for PubMed E-utilities.

    This class is responsible only for transport concerns such as request
    construction, timeout handling, retries, and response retrieval.
    """

    def __init__(self, timeout: int = 5, retries: int = 1) -> None:
        self._timeout = timeout
        self._retries = retries

    def search(self, query: str, max_results: int = 10, from_year: int | None = None, to_year: int | None = None) -> list[dict[str, Any]]:
        params = {
            "db": "pubmed",
            "retmode": "json",
            "retmax": max_results,
            "term": query,
        }
        if from_year is not None:
            params["mindate"] = str(from_year)
        if to_year is not None:
            params["maxdate"] = str(to_year)

        return self._request_json(PUBMED_SEARCH_ENDPOINT, params)

    def _request_json(self, url: str, params: dict[str, Any]) -> list[dict[str, Any]]:
        encoded = urlencode(params)
        request = Request(f"{url}?{encoded}", headers={"User-Agent": "Veritas/0.1"})

        for _ in range(max(1, self._retries)):
            try:
                with urlopen(request, timeout=self._timeout) as response:
                    payload = json.load(response)
                    return self._normalize_payload(payload)
            except Exception as exc:  # pragma: no cover - defensive path
                if self._retries <= 1:
                    raise ProviderUnavailableError(f"PubMed request failed: {exc}") from exc

        raise ProviderUnavailableError("PubMed request failed after retries")

    def _normalize_payload(self, payload: Any) -> list[dict[str, Any]]:
        if not isinstance(payload, dict):
            raise ProviderUnavailableError("Malformed PubMed response")

        if "esearchresult" not in payload:
            return []

        result = payload["esearchresult"]
        if not isinstance(result, dict):
            raise ProviderUnavailableError("Malformed PubMed response")

        ids = result.get("idlist", [])
        if not isinstance(ids, list):
            raise ProviderUnavailableError("Malformed PubMed response")

        return [{"id": item} for item in ids if isinstance(item, str)]
