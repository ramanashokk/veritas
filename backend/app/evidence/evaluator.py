from __future__ import annotations

from app.models.claim import Claim
from app.models.evidence_link import EvidenceRelationship
from app.models.observation import Observation


class ObservationEvaluator:
    """Deterministic evaluator for mapping observations to evidence relationships.

    The implementation uses simple keyword matching so it can run entirely on
    demo data without any AI or external services. It is intentionally easy to
    replace with a more sophisticated strategy later.
    """

    def evaluate(self, claim: Claim, observation: Observation) -> EvidenceRelationship:
        claim_text = claim.text.lower()
        observation_text = observation.text.lower()

        if self._contains_any(observation_text, ["increased", "higher risk", "worsen", "harm", "decreased"]):
            if self._contains_any(claim_text, ["reduce", "lowers", "reduces", "decrease", "lower"]):
                return EvidenceRelationship.CONTRADICTS

        if self._contains_any(observation_text, ["lower", "reduces", "reducing", "decrease", "decreases", "improve", "improves"]):
            if self._contains_any(claim_text, ["reduce", "lowers", "reduces", "decrease", "lower"]):
                return EvidenceRelationship.SUPPORTS

        if self._contains_any(observation_text, ["no association", "not associated", "no effect", "no evidence", "no impact"]):
            return EvidenceRelationship.NEUTRAL

        if self._contains_any(claim_text, ["reduce", "lowers", "reduces", "decrease", "lower"]) and self._contains_any(observation_text, ["risk", "disease", "cardiovascular", "mortality"]):
            return EvidenceRelationship.SUPPORTS

        if self._contains_any(claim_text, ["increase", "raises", "increases", "higher", "worse"]) and self._contains_any(observation_text, ["risk", "disease", "cardiovascular", "mortality"]):
            return EvidenceRelationship.CONTRADICTS

        return EvidenceRelationship.NEUTRAL

    def _contains_any(self, text: str, phrases: list[str]) -> bool:
        return any(phrase in text for phrase in phrases)
