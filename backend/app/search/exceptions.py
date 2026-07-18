class SearchError(Exception):
    """Base class for search-layer failures."""


class ProviderUnavailableError(SearchError):
    """Raised when a provider cannot be used for search."""


class InvalidSearchQueryError(SearchError):
    """Raised when a search query is invalid or empty."""
