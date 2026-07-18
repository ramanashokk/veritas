from dataclasses import dataclass
from enum import Enum


class EvidenceRelationship(str, Enum):
    """How an observation bears on a claim."""

    SUPPORTS = "supports"
    CONTRADICTS = "contradicts"
    NEUTRAL = "neutral"
    INCONCLUSIVE = "inconclusive"


@dataclass
class EvidenceLink:
    """The relationship between an Observation and a Claim.

    Evidence links preserve traceability: claim → observation → document → source.
    Each link records how a single neutral observation relates to a single claim.
    Links are relationships, not summaries.
    """

    id: str
    observation_id: str
    claim_id: str
    relationship: EvidenceRelationship
