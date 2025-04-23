from abc import abstractmethod
from datetime import date
from typing import Protocol

from weather_api.domain.dto import GetWeatherListDTO
from weather_api.domain.entities.weather import WeatherEntity
from weather_api.domain.enum import CityEnum


class IWeatherReader(Protocol):

    @abstractmethod
    async def get_weather_list(self, dto: GetWeatherListDTO) -> list[WeatherEntity]: ...

    @abstractmethod
    async def is_weather_data_exists(self, target_day: date) -> bool: ...


class IWeatherWriter(Protocol):

    @abstractmethod
    async def save_weather(self, weather: WeatherEntity) -> WeatherEntity | None: ...

    @abstractmethod
    async def commit(self) -> None: ...


class IWeatherFetcher(Protocol):

    @abstractmethod
    async def fetch_weather(self, city: CityEnum) -> WeatherEntity | None: ...
