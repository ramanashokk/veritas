from uuid import uuid4

from app.engine.claims import Claim
from app.engine.demo_data import get_demo_observation
from app.engine.evaluator import compute_consensus, evaluate_claim
from app.engine.evidence_link import EvidenceRelationship
from app.schemas.verify import ObservationResponse, VerifyResponse


class VerifyWorkflow:
    """Orchestrates claim verification through the Evidence Engine prototype."""

    def verify(self, claim_text: str) -> VerifyResponse:
        claim = Claim(id=str(uuid4()), text=claim_text)
        links = evaluate_claim(claim_text, claim.id)
        consensus = compute_consensus(claim.id, links)

        observations: list[ObservationResponse] = []
        for link in links:
            demo_observation = get_demo_observation(link.observation_id)
            if demo_observation is None:
                continue

            if link.relationship not in (
                EvidenceRelationship.SUPPORTS,
                EvidenceRelationship.CONTRADICTS,
            ):
                continue

            observations.append(
                ObservationResponse(
                    id=demo_observation.observation.id,
                    text=demo_observation.observation.text,
                    document=demo_observation.document.title,
                    publication_year=demo_observation.publication_year,
                    study_type=demo_observation.study_type,
                    relationship=link.relationship.value,
                )
            )

        return VerifyResponse(
            claim=claim.text,
            consensus=consensus.summary,
            supporting_observations=consensus.supporting_count,
            contradicting_observations=consensus.contradicting_count,
            observations=observations,
        )
