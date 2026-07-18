from __future__ import annotations

from app.evidence.summary import EvidenceSummary

from .result import ConsensusResult
from .strategy import ConsensusStrategy, SimpleConsensusStrategy


class ConsensusEngine:
    """Coordinates consensus evaluation using a pluggable strategy."""

    def __init__(self, strategy: ConsensusStrategy | None = None) -> None:
        self._strategy = strategy or SimpleConsensusStrategy()

    def evaluate(self, evidence_summary: EvidenceSummary) -> ConsensusResult:
        """Delegate consensus evaluation to the configured strategy."""

        return self._strategy.evaluate(evidence_summary)
