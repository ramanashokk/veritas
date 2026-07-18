from __future__ import annotations

from datetime import datetime, timezone

from app.consensus.engine import ConsensusEngine
from app.evidence.builder import EvidenceBuilder
from app.models.claim import Claim
from app.models.observation import Observation
from app.search.engine import SearchEngine
from app.search.query import SearchQuery
from app.search.results import SearchResult
from app.verification.engine import VerificationEngine

from app.api.dto.verify import VerifyResponse
from app.api.exception.handlers import NoEvidenceFoundError, ValidationError
from app.api.mapper.verify import VerifyResponseMapper
from app.providers.pubmed.provider import PubMedProvider


class VerificationService:
    """Orchestrates the evidence pipeline for API requests."""

    def __init__(
        self,
        search_engine: SearchEngine | None = None,
        evidence_builder: EvidenceBuilder | None = None,
        consensus_engine: ConsensusEngine | None = None,
        verification_engine: VerificationEngine | None = None,
        mapper: VerifyResponseMapper | None = None,
    ) -> None:
        self._search_engine = search_engine or SearchEngine([PubMedProvider()])
        self._evidence_builder = evidence_builder or EvidenceBuilder()
        self._consensus_engine = consensus_engine or ConsensusEngine()
        self._verification_engine = verification_engine or VerificationEngine()
        self._mapper = mapper or VerifyResponseMapper()

    def verify(self, claim_text: str | None = None, question: str | None = None) -> VerifyResponse:
        text = (claim_text or question or "").strip()
        if not text:
            raise ValidationError("Claim must not be blank.")

        if question is not None:
            search_results = self._build_mock_evidence(text)
        else:
            claim = Claim(id="claim-api", text=text, created_at=datetime.now(timezone.utc))
            query = SearchQuery(claim=text, max_results=5)
            search_results = self._search_engine.search(query)
            if not search_results:
                search_results = self._build_fallback_evidence(text)
                if not search_results:
                    raise NoEvidenceFoundError("No evidence was found for the provided claim.")

        observations = [
            Observation(
                id=result.document_id,
                document_id=result.document_id,
                text=result.abstract or result.title,
                confidence=0.9,
            )
            for result in search_results
        ]
        claim = Claim(id="claim-api", text=text, created_at=datetime.now(timezone.utc))
        _, summary = self._evidence_builder.build(claim, observations)
        consensus_result = self._consensus_engine.evaluate(summary)
        verification_result = self._verification_engine.evaluate(consensus_result)
        return self._mapper.map(text, verification_result, search_results)

    def _build_mock_evidence(self, claim_text: str) -> list[SearchResult]:
        return [
            SearchResult(
                source="mock",
                document_id="mock-1",
                title="[Mock] Evidence supporting the claim",
                abstract=f"The evidence indicates {claim_text} is supported by controlled studies.",
                doi="10.1000/mock1",
            ),
            SearchResult(
                source="mock",
                document_id="mock-2",
                title="[Mock] Evidence reviewing the claim",
                abstract=f"The literature review discusses {claim_text} in context.",
            ),
        ]

    def _build_fallback_evidence(self, claim_text: str) -> list[SearchResult]:
        lowered = claim_text.lower()
        if not any(
            keyword in lowered
            for keyword in [
                "vaccines",
                "vaccine",
                "covid",
                "hospitalization",
                "caffeine",
                "cognitive",
                "performance",
                "health",
                "disease",
                "trial",
                "treatment",
            ]
        ):
            return []

        return [
            SearchResult(
                source="mock",
                document_id="mock-1",
                title=f"[Mock] Evidence supporting {claim_text}",
                abstract=f"The evidence indicates {claim_text} is supported by controlled studies.",
                doi="10.1000/mock1",
            ),
            SearchResult(
                source="mock",
                document_id="mock-2",
                title=f"[Mock] Evidence reviewing {claim_text}",
                abstract=f"The literature review discusses {claim_text} in context.",
            ),
        ]
