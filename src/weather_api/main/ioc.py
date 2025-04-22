from typing import AsyncIterable

from dishka import Scope, Provider, from_context, provide
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from weather_api.application.interfaces import IWeatherReader
from weather_api.application.use_cases.get_stats_use_case import GetStatsUseCase
from weather_api.application.use_cases.get_weather_list_use_case import (
    GetWeatherListUseCase,
)
from weather_api.config import Config
from weather_api.infrastructure.database.gateway.reader import WeatherDataReader
from weather_api.infrastructure.database.session_factory import get_session_maker


class AppProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_session_maker(self, config: Config) -> async_sessionmaker[AsyncSession]:
        return get_session_maker(config.postgres)

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self, session_maker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with session_maker() as session:
            yield session

    reader_gateway = provide(
        WeatherDataReader, scope=Scope.REQUEST, provides=IWeatherReader
    )

    get_weather_list_uc = provide(GetWeatherListUseCase, scope=Scope.REQUEST)
    get_stats_uc = provide(GetStatsUseCase, scope=Scope.REQUEST)
