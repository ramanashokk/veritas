from __future__ import annotations

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

from app.search.exceptions import InvalidSearchQueryError, ProviderUnavailableError


class VerificationError(Exception):
    """Base error for verification workflow failures."""


class NoEvidenceFoundError(VerificationError):
    """Raised when no evidence is available for a claim."""


class ValidationError(VerificationError):
    """Raised when request validation fails."""


async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    errors = exc.errors()
    if any(error.get("type") == "json_invalid" for error in errors):
        return JSONResponse(
            status_code=HTTP_400_BAD_REQUEST,
            content={
                "timestamp": "now",
                "status": 400,
                "error": "Validation Error",
                "message": "Invalid JSON payload.",
            },
        )

    return JSONResponse(
        status_code=422,
        content={
            "timestamp": "now",
            "status": 422,
            "error": "Validation Error",
            "message": "Invalid request payload.",
        },
    )


async def verification_exception_handler(request: Request, exc: VerificationError) -> JSONResponse:
    if isinstance(exc, NoEvidenceFoundError):
        return JSONResponse(
            status_code=HTTP_404_NOT_FOUND,
            content={
                "timestamp": "now",
                "status": 404,
                "error": "No Evidence Found",
                "message": str(exc),
            },
        )

    if isinstance(exc, ValidationError):
        return JSONResponse(
            status_code=HTTP_400_BAD_REQUEST,
            content={
                "timestamp": "now",
                "status": 400,
                "error": "Validation Error",
                "message": str(exc),
            },
        )

    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "timestamp": "now",
            "status": 500,
            "error": "Internal Server Error",
            "message": str(exc),
        },
    )


async def provider_exception_handler(request: Request, exc: ProviderUnavailableError) -> JSONResponse:
    return JSONResponse(
        status_code=HTTP_404_NOT_FOUND,
        content={
            "timestamp": "now",
            "status": 404,
            "error": "No Evidence Found",
            "message": "No evidence could be retrieved from available providers.",
        },
    )


async def invalid_query_exception_handler(request: Request, exc: InvalidSearchQueryError) -> JSONResponse:
    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={
            "timestamp": "now",
            "status": 400,
            "error": "Validation Error",
            "message": str(exc),
        },
    )
