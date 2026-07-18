from fastapi import APIRouter

from app.api.controller.verify import api_router as verify_api_router

api_router = APIRouter(prefix="/api/v1")


@api_router.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


api_router.include_router(verify_api_router)
