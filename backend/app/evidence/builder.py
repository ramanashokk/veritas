from __future__ import annotations

from app.models.claim import Claim
from app.models.evidence_link import EvidenceLink, EvidenceRelationship
from app.models.observation import Observation

from .evaluator import ObservationEvaluator
from .summary import EvidenceSummary


class EvidenceBuilder:
    """Build evidence links from a claim and a set of observations.

    This component is intentionally deterministic and domain-focused. It never
    needs to know where observations originated, only how to evaluate them.
    """

    def __init__(self, evaluator: ObservationEvaluator | None = None) -> None:
        self._evaluator = evaluator or ObservationEvaluator()

    def build(self, claim: Claim, observations: list[Observation]) -> tuple[list[EvidenceLink], EvidenceSummary]:
        links: list[EvidenceLink] = []
        for observation in observations:
            relationship = self._evaluator.evaluate(claim, observation)
            links.append(
                EvidenceLink(
                    observation_id=observation.id,
                    claim_id=claim.id,
                    relationship=relationship,
                )
            )

        support_count = sum(1 for link in links if link.relationship is EvidenceRelationship.SUPPORTS)
        contradict_count = sum(1 for link in links if link.relationship is EvidenceRelationship.CONTRADICTS)
        neutral_count = sum(1 for link in links if link.relationship is EvidenceRelationship.NEUTRAL)
        total_count = len(links)
        confidence = support_count / total_count if total_count else 0.0

        summary = EvidenceSummary(
            claim_id=claim.id,
            support_count=support_count,
            contradict_count=contradict_count,
            neutral_count=neutral_count,
            confidence=confidence,
        )
        return links, summary
