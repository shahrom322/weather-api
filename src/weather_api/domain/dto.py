from dataclasses import dataclass
from datetime import date

from weather_api.domain.entities.weather import WeatherEntity
from weather_api.domain.enum import CityEnum
from weather_api.domain.types import CelsiusType, HumidityType


@dataclass
class ListWeatherDTO:
    data: list[WeatherEntity]


@dataclass
class StatsDTO:
    avg_temperature: CelsiusType
    avg_humidity: HumidityType


@dataclass
class GetWeatherListDTO:
    start_date: date
    end_date: date
    city: CityEnum
