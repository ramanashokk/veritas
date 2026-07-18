from dataclasses import dataclass


@dataclass
class Source:
    """Represents where information originates.

    A source is an external system or corpus — for example PubMed, OpenAlex,
    ClinicalTrials.gov, USPTO, or WHO. Sources provide documents; they do not
    contain interpretations or conclusions.
    """

    id: str
    name: str
    description: str | None = None
