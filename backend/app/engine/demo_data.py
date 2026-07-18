from dataclasses import dataclass
from datetime import datetime

from app.engine.document import Document, DocumentType
from app.engine.observation import Observation
from app.engine.source import Source


@dataclass
class DemoObservation:
    """Prototype observation bundled with document metadata for in-memory evaluation."""

    observation: Observation
    document: Document
    publication_year: int
    study_type: str


DEMO_SOURCE = Source(
    id="source-demo",
    name="Demo Corpus",
    description="In-memory prototype dataset. Not connected to external APIs.",
)

DEMO_DOCUMENTS: dict[str, Document] = {
    "doc-1": Document(
        id="doc-1",
        source_id=DEMO_SOURCE.id,
        title="Long-term coffee intake and cardiovascular mortality (cohort study)",
        document_type=DocumentType.PAPER,
        published_at=datetime(2015, 1, 1),
    ),
    "doc-2": Document(
        id="doc-2",
        source_id=DEMO_SOURCE.id,
        title="Coffee consumption and cardiovascular outcomes: a meta-analysis",
        document_type=DocumentType.PAPER,
        published_at=datetime(2018, 6, 1),
    ),
    "doc-3": Document(
        id="doc-3",
        source_id=DEMO_SOURCE.id,
        title="Coffee intake and cardiovascular mortality in a large prospective cohort",
        document_type=DocumentType.PAPER,
        published_at=datetime(2020, 3, 1),
    ),
    "doc-4": Document(
        id="doc-4",
        source_id=DEMO_SOURCE.id,
        title="Physical activity and all-cause mortality: randomized controlled trial",
        document_type=DocumentType.TRIAL,
        published_at=datetime(2017, 9, 1),
    ),
    "doc-5": Document(
        id="doc-5",
        source_id=DEMO_SOURCE.id,
        title="Exercise and mortality: systematic review",
        document_type=DocumentType.PAPER,
        published_at=datetime(2021, 2, 1),
    ),
}

DEMO_OBSERVATIONS: dict[str, DemoObservation] = {
    "obs-1": DemoObservation(
        observation=Observation(
            id="obs-1",
            document_id="doc-1",
            text="Higher habitual coffee intake was associated with lower cardiovascular mortality in the cohort.",
        ),
        document=DEMO_DOCUMENTS["doc-1"],
        publication_year=2015,
        study_type="cohort study",
    ),
    "obs-2": DemoObservation(
        observation=Observation(
            id="obs-2",
            document_id="doc-2",
            text="Pooled analysis reported an inverse association between moderate coffee intake and cardiovascular mortality.",
        ),
        document=DEMO_DOCUMENTS["doc-2"],
        publication_year=2018,
        study_type="meta-analysis",
    ),
    "obs-3": DemoObservation(
        observation=Observation(
            id="obs-3",
            document_id="doc-3",
            text="No statistically significant association was found between coffee intake and cardiovascular mortality.",
        ),
        document=DEMO_DOCUMENTS["doc-3"],
        publication_year=2020,
        study_type="cohort study",
    ),
    "obs-4": DemoObservation(
        observation=Observation(
            id="obs-4",
            document_id="doc-4",
            text="The intervention group showed lower all-cause mortality than the control group.",
        ),
        document=DEMO_DOCUMENTS["doc-4"],
        publication_year=2017,
        study_type="randomized controlled trial",
    ),
    "obs-5": DemoObservation(
        observation=Observation(
            id="obs-5",
            document_id="doc-5",
            text="Regular exercise was consistently associated with reduced all-cause mortality across included studies.",
        ),
        document=DEMO_DOCUMENTS["doc-5"],
        publication_year=2021,
        study_type="systematic review",
    ),
}


def get_demo_observation(observation_id: str) -> DemoObservation | None:
    return DEMO_OBSERVATIONS.get(observation_id)
