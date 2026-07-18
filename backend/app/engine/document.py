from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class DocumentType(str, Enum):
    """Kind of artifact retrieved from a source."""

    PAPER = "paper"
    PATENT = "patent"
    TRIAL = "trial"
    GUIDELINE = "guideline"
    REPORT = "report"
    JUDGMENT = "judgment"


@dataclass
class Document:
    """A paper, patent, trial, guideline, report, or judgment.

    Documents are the primary artifacts of evidence. Every observation must
    trace back to a document, and every document must trace back to a source.
    """

    id: str
    source_id: str
    title: str
    document_type: DocumentType
    external_id: str | None = None
    url: str | None = None
    published_at: datetime | None = None
