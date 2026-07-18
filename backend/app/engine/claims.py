from dataclasses import dataclass


@dataclass
class Claim:
    """A proposition that can be evaluated using observations.

    Claims are evaluable statements — they can be supported, contradicted,
    or left inconclusive by evidence. A user's question becomes a claim
    inside the Evidence Engine.
    """

    id: str
    text: str
