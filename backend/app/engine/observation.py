from dataclasses import dataclass


@dataclass
class Observation:
    """A factual observation extracted from a document.

    Observations remain neutral. They describe what a document states or what
    was measured — without inference, opinion, or evaluative language.
    Observations are facts, not conclusions.
    """

    id: str
    document_id: str
    text: str
    excerpt: str | None = None
