from __future__ import annotations

from fastapi import APIRouter, Depends

from app.api.dto.verify import VerifyRequest, VerifyResponse
from app.api.service.verify import VerificationService

api_router = APIRouter()


def get_service() -> VerificationService:
    return VerificationService()


@api_router.post("/verify", response_model=VerifyResponse)
def verify(request: VerifyRequest, service: VerificationService = Depends(get_service)) -> VerifyResponse:
    return service.verify(claim_text=request.claim, question=request.question)
