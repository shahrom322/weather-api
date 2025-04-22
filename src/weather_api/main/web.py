import dishka
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from weather_api.config import Config
from weather_api.main.ioc import AppProvider
from weather_api.presentation.http.router import api_router
from weather_api.presentation.types import tags_metadata

config = Config()
container = make_async_container(AppProvider(), context={Config: config})


def create_app() -> FastAPI:
    app = FastAPI(title=config.application.app_name, openapi_tags=tags_metadata)
    app.include_router(api_router, prefix="/api/v1")

    setup_dishka(container=container, app=app)

    return app
