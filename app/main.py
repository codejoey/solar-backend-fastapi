"""
- Set up `FastAPI`Application
    - Exception Handler for exception handling
    - Middleware for additional processing for every request
- Good to know
    - https://fastapi.tiangolo.com/tutorial/first-steps/
    - https://fastapi.tiangolo.com/tutorial/middleware/
    - https://fastapi.tiangolo.com/tutorial/handling-errors/
"""

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import config
from app.core.errors.error import BaseAPIException, BaseAuthException
from app.core.errors.handler import api_error_handler, api_auth_error_handler
from app.routers import router


def get_application() -> FastAPI:
    application = FastAPI(default_response_class=ORJSONResponse, **config.fastapi_kwargs)

    application.include_router(router)
    application.add_exception_handler(BaseAPIException, api_error_handler)
    application.add_exception_handler(BaseAuthException, api_auth_error_handler)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application

app = get_application()
