from fastapi import FastAPI
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from weather_api.domain.exceptions import InvalidDateRangeError


async def invalid_date_range_handler(_: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        content={"detail": str(exc)}, status_code=status.HTTP_400_BAD_REQUEST
    )


def setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(InvalidDateRangeError, invalid_date_range_handler)
