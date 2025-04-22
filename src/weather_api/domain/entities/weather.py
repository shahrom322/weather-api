from dataclasses import dataclass
from datetime import datetime

from weather_api.domain.enum import CityEnum
from weather_api.domain.types import CelsiusType, HumidityType


@dataclass
class WeatherEntity:
    city: CityEnum
    date: datetime
    temperature: CelsiusType
    humidity: HumidityType
