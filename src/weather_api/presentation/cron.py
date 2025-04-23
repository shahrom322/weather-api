from logging import getLogger

from dishka import FromDishka
from dishka.integrations.arq import inject

from weather_api.application.use_cases.fetch_weather_use_case import FetchWeatherUseCase
from weather_api.application.use_cases.is_weather_data_exists_use_case import (
    IsWeatherDataExistsUseCase,
)

logger = getLogger(__name__)


@inject
async def fetch_weather_cron(_, use_case: FromDishka[FetchWeatherUseCase]) -> None:
    await use_case()
    logger.info(f"Данные о погоде получены")


@inject
async def alert_missing_weather_data(
    _, use_case: FromDishka[IsWeatherDataExistsUseCase]
) -> None:
    if await use_case() is False:
        logger.warning("Данные о погоде за последние сутки отсутствуют в хранилище")
        return

    logger.info("Данные о погоде за последние сутки присутствуют в хранилище")
