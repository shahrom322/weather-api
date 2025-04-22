from typing import Annotated
from datetime import date

from pydantic import BaseModel, Field

from weather_api.domain.enum import CityEnum
from weather_api.domain.types import CelsiusType, HumidityType


class WeatherOutputModel(BaseModel):
    city: Annotated[
        CityEnum,
        Field(..., description="Город, для которого сняты показания"),
    ]
    date: Annotated[
        date,
        Field(
            ..., examples=["2025-03-11"], description="Дата замера в формате YYYY-MM-DD"
        ),
    ]
    temperature: Annotated[
        CelsiusType,
        Field(
            ...,
            examples=[14.00, 36.60],
            description="Температура в градусах Цельсия (2 знака после точки)",
        ),
    ]
    humidity: Annotated[
        HumidityType,
        Field(..., examples=[80], description="Влажность в процентах (0–100)"),
    ]


class ListWeatherOutputModel(BaseModel):
    data: Annotated[
        list[WeatherOutputModel], Field(description="Список данных о погоде")
    ]
