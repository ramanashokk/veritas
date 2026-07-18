from datetime import UTC, datetime
from uuid import uuid4

from app.engine.consensus import Consensus
from app.engine.demo_data import get_demo_observation
from app.engine.evidence_link import EvidenceLink, EvidenceRelationship

# Hardcoded prototype mappings: exact claim text -> observation relationships.
# No NLP, fuzzy matching, or AI — architectural prototype only.
CLAIM_OBSERVATION_MAPPINGS: dict[str, dict[str, EvidenceRelationship]] = {
    "Coffee reduces cardiovascular mortality": {
        "obs-1": EvidenceRelationship.SUPPORTS,
        "obs-2": EvidenceRelationship.SUPPORTS,
        "obs-3": EvidenceRelationship.CONTRADICTS,
    },
    "Regular exercise reduces all-cause mortality": {
        "obs-4": EvidenceRelationship.SUPPORTS,
        "obs-5": EvidenceRelationship.SUPPORTS,
    },
    "Saturated fat causes heart disease": {
        "obs-1": EvidenceRelationship.SUPPORTS,
        "obs-3": EvidenceRelationship.CONTRADICTS,
    },
    "Vitamin E slows aging": {},
}


def evaluate_claim(claim_text: str, claim_id: str) -> list[EvidenceLink]:
    """Evaluate a claim against the in-memory observation dataset."""
    mappings = CLAIM_OBSERVATION_MAPPINGS.get(claim_text)
    if mappings is None:
        return []

    links: list[EvidenceLink] = []
    for observation_id, relationship in mappings.items():
        if get_demo_observation(observation_id) is None:
            continue

        links.append(
            EvidenceLink(
                id=str(uuid4()),
                observation_id=observation_id,
                claim_id=claim_id,
                relationship=relationship,
            )
        )

    return links


def compute_consensus(claim_id: str, links: list[EvidenceLink]) -> Consensus:
    """Derive consensus summary from evidence link counts."""
    supporting_count = sum(
        1 for link in links if link.relationship == EvidenceRelationship.SUPPORTS
    )
    contradicting_count = sum(
        1 for link in links if link.relationship == EvidenceRelationship.CONTRADICTS
    )
    neutral_count = sum(
        1 for link in links if link.relationship == EvidenceRelationship.NEUTRAL
    )
    inconclusive_count = sum(
        1 for link in links if link.relationship == EvidenceRelationship.INCONCLUSIVE
    )

    if supporting_count == 0:
        summary = "No evidence"
    elif supporting_count == contradicting_count:
        summary = "Mixed evidence"
    elif contradicting_count == 0:
        summary = "Strong support"
    elif supporting_count > contradicting_count:
        summary = "Moderate support"
    else:
        summary = "Mixed evidence"

    return Consensus(
        claim_id=claim_id,
        summary=summary,
        supporting_count=supporting_count,
        contradicting_count=contradicting_count,
        neutral_count=neutral_count,
        inconclusive_count=inconclusive_count,
        computed_at=datetime.now(UTC),
    )
