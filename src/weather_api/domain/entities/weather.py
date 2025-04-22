from dataclasses import dataclass
from datetime import date

from weather_api.domain.enum import CityEnum
from weather_api.domain.types import CelsiusType, HumidityType


@dataclass
class WeatherEntity:
    city: CityEnum
    date: date
    temperature: CelsiusType
    humidity: HumidityType
