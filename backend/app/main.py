from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from app.api.exception.handlers import (
    invalid_query_exception_handler,
    provider_exception_handler,
    validation_exception_handler,
    verification_exception_handler,
)
from app.api.exception.handlers import VerificationError
from app.api.router import api_router
from app.config import settings
from app.search.exceptions import InvalidSearchQueryError, ProviderUnavailableError

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(VerificationError, verification_exception_handler)
app.add_exception_handler(ProviderUnavailableError, provider_exception_handler)
app.add_exception_handler(InvalidSearchQueryError, invalid_query_exception_handler)

app.include_router(api_router)
