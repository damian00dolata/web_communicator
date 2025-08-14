from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
import traceback
from logger import logger

def add_exception_handlers(app: FastAPI, debug: bool = False):

    @app.exception_handler(RequestValidationError)
    async def validation_handler(request: Request, exc: RequestValidationError):
        logger.warning("Validation error", extra={"extra_data": {"errors": exc.errors(), "path": str(request.url)}})
        return JSONResponse(
            status_code=422,
            content={
                "type": "validation-error",
                "title": "Request validation failed",
                "status": 422,
                "detail": "One or more request fields are invalid",
                "instance": str(request.url),
                "errors": exc.errors()
            }
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        logger.error("HTTP exception", extra={"extra_data": {"status": exc.status_code, "detail": exc.detail, "path": str(request.url)}})
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "type": "http-error",
                "title": "HTTP Exception",
                "status": exc.status_code,
                "detail": exc.detail,
                "instance": str(request.url)
            }
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        tb_str = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
        logger.error("Unhandled exception", exc_info=exc, extra={"extra_data": {"path": str(request.url)}})
        payload = {
            "type": "internal-exception",
            "title": "Internal Server Error",
            "status": 500,
            "detail": "An internal server error occurred.",
            "instance": str(request.url)
        }
        if debug:
            payload["traceback"] = tb_str
        return JSONResponse(status_code=500, content=payload)
