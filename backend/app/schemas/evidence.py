from pydantic import BaseModel


class Evidence(BaseModel):
    title: str
    source: str
    summary: str
    url: str | None = None
    pubmed_id: str | None = None
