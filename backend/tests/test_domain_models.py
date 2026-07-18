import pytest
from pydantic import ValidationError

from app.models.claim import Claim
from app.models.consensus import Consensus, ConsensusLabel
from app.models.document import Document
from app.models.evidence_link import EvidenceLink, EvidenceRelationship
from app.models.observation import Observation
from app.models.source import Source


def test_domain_models_are_immutable_and_structured() -> None:
    source = Source(
        id="src-1",
        name="PubMed",
        type="database",
        url="https://pubmed.ncbi.nlm.nih.gov",
        metadata={"country": "US"},
    )
    document = Document(
        id="doc-1",
        source_id=source.id,
        title="Clinical Study",
        authors=["Ada Lovelace"],
        publication_date="2024-01-01",
        identifier="doi:10.1234/example",
        abstract="A summary of the study.",
        metadata={"journal": "Nature"},
    )
    observation = Observation(
        id="obs-1",
        document_id=document.id,
        text="The trial reported a 12% reduction.",
        confidence=0.91,
        metadata={"section": "abstract"},
    )
    claim = Claim(id="claim-1", text="The treatment is effective.", created_at="2024-01-02")
    evidence_link = EvidenceLink(
        observation_id=observation.id,
        claim_id=claim.id,
        relationship=EvidenceRelationship.SUPPORTS,
    )
    consensus = Consensus(
        claim_id=claim.id,
        support_count=1,
        contradict_count=0,
        neutral_count=0,
        confidence=0.91,
        label=ConsensusLabel.SUPPORTS,
    )

    assert source.name == "PubMed"
    assert document.source_id == source.id
    assert observation.document_id == document.id
    assert evidence_link.relationship is EvidenceRelationship.SUPPORTS
    assert consensus.label is ConsensusLabel.SUPPORTS

    with pytest.raises(ValidationError):
        source.name = "Changed"
