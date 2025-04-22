from typing import AsyncIterable

import httpx
from dishka import Scope, Provider, from_context, provide
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from weather_api.application.interfaces import (
    IWeatherReader,
    IWeatherFetcher,
    IWeatherWriter,
)
from weather_api.application.use_cases.fetch_weather_use_case import FetchWeatherUseCase
from weather_api.application.use_cases.get_stats_use_case import GetStatsUseCase
from weather_api.application.use_cases.get_weather_list_use_case import (
    GetWeatherListUseCase,
)
from weather_api.config import Config, OpenWeatherConfig
from weather_api.infrastructure.clients.open_weather_client import OpenWeatherClient
from weather_api.infrastructure.database.gateway.reader import WeatherDataReader
from weather_api.infrastructure.database.gateway.writer import WeatherDataWriter
from weather_api.infrastructure.database.session_factory import get_session_maker


class AppProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_openweather_config(self, config: Config) -> OpenWeatherConfig:
        return config.openweather

    @provide(scope=Scope.APP)
    def get_session_maker(self, config: Config) -> async_sessionmaker[AsyncSession]:
        return get_session_maker(config.postgres)

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self, session_maker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with session_maker() as session:
            yield session

    @provide(scope=Scope.REQUEST)
    async def get_httpx_client(self) -> AsyncIterable[httpx.AsyncClient]:
        async with httpx.AsyncClient() as client:
            yield client

    fetch_client = provide(
        OpenWeatherClient, scope=Scope.REQUEST, provides=IWeatherFetcher
    )
    writer_gateway = provide(
        WeatherDataWriter, scope=Scope.REQUEST, provides=IWeatherWriter
    )
    reader_gateway = provide(
        WeatherDataReader, scope=Scope.REQUEST, provides=IWeatherReader
    )

    get_weather_list_uc = provide(GetWeatherListUseCase, scope=Scope.REQUEST)
    get_stats_uc = provide(GetStatsUseCase, scope=Scope.REQUEST)
    fetch_weather_uc = provide(FetchWeatherUseCase, scope=Scope.REQUEST)
