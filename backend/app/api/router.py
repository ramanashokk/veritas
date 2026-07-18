from fastapi import APIRouter

from app.schemas.verify import VerifyRequest, VerifyResponse
from app.workflows.verify import VerifyWorkflow

api_router = APIRouter(prefix="/api/v1")
verify_workflow = VerifyWorkflow()


@api_router.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@api_router.post("/verify", response_model=VerifyResponse)
def verify(request: VerifyRequest) -> VerifyResponse:
    return verify_workflow.verify(request.claim)
