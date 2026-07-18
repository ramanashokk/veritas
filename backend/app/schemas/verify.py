from pydantic import BaseModel, Field


class ObservationResponse(BaseModel):
    id: str
    text: str
    document: str
    publication_year: int
    study_type: str
    relationship: str


class VerifyRequest(BaseModel):
    claim: str = Field(..., min_length=1, description="Claim to evaluate against evidence")


class VerifyResponse(BaseModel):
    claim: str
    consensus: str
    supporting_observations: int
    contradicting_observations: int
    observations: list[ObservationResponse]
