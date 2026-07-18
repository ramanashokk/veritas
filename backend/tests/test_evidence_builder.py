from datetime import datetime

from app.evidence.builder import EvidenceBuilder
from app.models.claim import Claim
from app.models.evidence_link import EvidenceRelationship
from app.models.observation import Observation


def test_supported_claim() -> None:
    builder = EvidenceBuilder()
    claim = Claim(id="claim-1", text="Coffee reduces heart disease.", created_at=datetime(2024, 1, 1))
    observation = Observation(
        id="obs-1",
        document_id="doc-1",
        text="Several studies show coffee consumption lowers cardiovascular risk.",
        confidence=0.95,
    )

    links, summary = builder.build(claim, [observation])

    assert len(links) == 1
    assert links[0].relationship is EvidenceRelationship.SUPPORTS
    assert summary.support_count == 1
    assert summary.confidence == 1.0


def test_contradicted_claim() -> None:
    builder = EvidenceBuilder()
    claim = Claim(id="claim-2", text="Coffee reduces heart disease.", created_at=datetime(2024, 1, 1))
    observation = Observation(
        id="obs-2",
        document_id="doc-2",
        text="Coffee consumption increased cardiovascular risk.",
        confidence=0.9,
    )

    links, summary = builder.build(claim, [observation])

    assert links[0].relationship is EvidenceRelationship.CONTRADICTS
    assert summary.contradict_count == 1
    assert summary.confidence == 0.0


def test_mixed_evidence() -> None:
    builder = EvidenceBuilder()
    claim = Claim(id="claim-3", text="Coffee reduces heart disease.", created_at=datetime(2024, 1, 1))
    observations = [
        Observation(id="obs-3", document_id="doc-3", text="Several studies show coffee consumption lowers cardiovascular risk.", confidence=0.95),
        Observation(id="obs-4", document_id="doc-4", text="No association was found between coffee and cardiovascular disease.", confidence=0.8),
        Observation(id="obs-5", document_id="doc-5", text="Coffee consumption increased cardiovascular risk.", confidence=0.91),
    ]

    links, summary = builder.build(claim, observations)

    assert [link.relationship for link in links] == [
        EvidenceRelationship.SUPPORTS,
        EvidenceRelationship.NEUTRAL,
        EvidenceRelationship.CONTRADICTS,
    ]
    assert summary.support_count == 1
    assert summary.contradict_count == 1
    assert summary.neutral_count == 1
    assert summary.confidence == 1 / 3


def test_no_evidence() -> None:
    builder = EvidenceBuilder()
    claim = Claim(id="claim-4", text="Coffee reduces heart disease.", created_at=datetime(2024, 1, 1))

    links, summary = builder.build(claim, [])

    assert links == []
    assert summary.support_count == 0
    assert summary.contradict_count == 0
    assert summary.neutral_count == 0
    assert summary.confidence == 0.0
