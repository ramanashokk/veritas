from dataclasses import dataclass
from datetime import datetime


@dataclass
class Consensus:
    """A view computed from multiple EvidenceLinks for a claim.

    Consensus synthesizes the pattern of supporting, contradicting, neutral,
    and inconclusive links. It is a derived view — never stored or presented
    as fixed truth. It may change as new evidence arrives or is re-evaluated.
    """

    claim_id: str
    summary: str
    supporting_count: int = 0
    contradicting_count: int = 0
    neutral_count: int = 0
    inconclusive_count: int = 0
    computed_at: datetime | None = None
