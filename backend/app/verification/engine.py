from __future__ import annotations

from app.consensus.result import ConsensusResult

from .rules import VerificationRule, SimpleVerificationRule


class VerificationEngine:
    """Coordinates verification using a pluggable rule strategy."""

    def __init__(self, rule: VerificationRule | None = None) -> None:
        self._rule = rule or SimpleVerificationRule()

    def evaluate(self, consensus_result: ConsensusResult) -> "VerificationResult":
        """Delegate verification decision logic to the configured rule."""

        return self._rule.evaluate(consensus_result)
