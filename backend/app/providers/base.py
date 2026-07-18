from __future__ import annotations

from abc import ABC, abstractmethod

from app.search.interfaces import SearchProvider


class BaseProvider(SearchProvider, ABC):
    """Reusable base class for provider implementations.

    Provider-specific behavior should be implemented in subclasses by combining
    a client, parser, and mapper while keeping the public SearchProvider
    interface stable.
    """

    @abstractmethod
    def search(self, query):
        raise NotImplementedError
