from abc import abstractmethod
from typing import Protocol

from weather_api.domain.dto import GetWeatherListDTO
from weather_api.domain.entities.weather import WeatherEntity


class IWeatherReader(Protocol):

    @abstractmethod
    async def get_weather_list(self, dto: GetWeatherListDTO) -> list[WeatherEntity]: ...
