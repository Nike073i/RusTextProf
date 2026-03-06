from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from .exceptions import AppError
from .schemas import ErrorResponse
import logging

logger = logging.getLogger(__name__)

def setup_error_handlers(app: FastAPI):
    @app.exception_handler(AppError)
    async def app_error_handler(request: Request, exc: AppError):
        logger.warning(f"App error ({exc.code}): {exc.message}")
        
        response = ErrorResponse(
            error={
                "code": exc.code,
                "message": exc.message,
                "details": exc.details
            },
            path=request.url.path
        )
        
        return JSONResponse(
            status_code=exc.status_code,
            content=response.model_dump()
        )
    
    @app.exception_handler(RequestValidationError)
    async def validation_error_handler(request: Request, exc: RequestValidationError):
        logger.info(f"Validation error: {exc.errors()}")
        
        errors = []
        for error in exc.errors():
            errors.append({
                "field": ".".join(str(loc) for loc in error["loc"]),
                "message": error["msg"],
                "code": error["type"]
            })
        
        response = ErrorResponse(
            error={
                "code": "request_validation_error",
                "message": "Ошибка валидации запроса",
                "details": {"errors": errors}
            },
            path=request.url.path
        )
        
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=response.model_dump()
        )
    
    @app.exception_handler(Exception)
    async def generic_error_handler(request: Request, exc: Exception):
        logger.error(f"Unexpected error: {str(exc)}", exc_info=True)
        
        response = ErrorResponse(
            error={
                "code": "internal_server_error",
                "message": "Внутренняя ошибка сервера",
                "details": {"debug": str(exc) if app.debug else None}
            },
            path=request.url.path
        )
        
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=response.model_dump()
        )
