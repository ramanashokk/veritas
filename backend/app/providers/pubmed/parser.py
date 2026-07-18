from __future__ import annotations

from typing import Any


class PubMedParser:
    """Transforms raw PubMed payloads into intermediate Python objects.

    This layer intentionally does not create SearchResult instances; it only
    converts provider responses into a simple structured form.
    """

    def parse(self, payload: Any) -> list[dict[str, Any]]:
        if not isinstance(payload, dict):
            return []

        records: list[dict[str, Any]] = []
        for item in payload.get("results", []) or []:
            if isinstance(item, dict):
                records.append(item)
        return records
