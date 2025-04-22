from datetime import date
from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Query

from weather_api.application.use_cases.get_weather_list_use_case import (
    GetWeatherListUseCase,
)
from weather_api.domain.dto import ListWeatherDTO, GetWeatherListDTO
from weather_api.domain.enum import CityEnum
from weather_api.presentation.http.output_models import ListWeatherOutputModel
from weather_api.presentation.types import Tags

api_router = APIRouter(tags=[Tags.base])


@api_router.get(
    "/weather",
    response_model=ListWeatherOutputModel,
    summary="Получить погодные данные",
)
@inject
async def get_weather(
    start_date: Annotated[date, Query(description="Дата начала, формат YYYY-MM-DD")],
    end_date: Annotated[date, Query(description="Дата конца, формат YYYY-MM-DD")],
    city: Annotated[CityEnum, Query(description="Город")],
    use_case: FromDishka[GetWeatherListUseCase],
) -> ListWeatherDTO:
    """
    Возвращает список записей о погоде для указанного города за диапазон дат включительно
    """
    dto = GetWeatherListDTO(start_date=start_date, end_date=end_date, city=city)
    return await use_case(dto)
