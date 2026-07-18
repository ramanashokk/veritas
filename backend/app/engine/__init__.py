"""Evidence Engine — core domain model for evidence retrieval and synthesis."""

from app.engine.claims import Claim
from app.engine.consensus import Consensus
from app.engine.document import Document, DocumentType
from app.engine.evidence_link import EvidenceLink, EvidenceRelationship
from app.engine.observation import Observation
from app.engine.source import Source

__all__ = [
    "Claim",
    "Consensus",
    "Document",
    "DocumentType",
    "EvidenceLink",
    "EvidenceRelationship",
    "Observation",
    "Source",
]
