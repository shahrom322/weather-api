from datetime import date
from typing import Tuple

import httpx
from httpx import HTTPStatusError
from pydantic import ValidationError

from weather_api.application.interfaces import IWeatherFetcher
from weather_api.config import OpenWeatherConfig
from weather_api.domain.entities.weather import WeatherEntity
from weather_api.domain.enum import CityEnum
from weather_api.infrastructure.clients.response_validators import FetchWeatherData

LAT_LONG_BY_CITY_MAPPING: dict[CityEnum, Tuple[str, str]] = {
    CityEnum.TOKYO: ("35.6895", "139.6917"),
    CityEnum.LONDON: ("51.5085", "-0.1257"),
    CityEnum.MOSCOW: ("55.7522", "37.6156"),
}


class OpenWeatherClient(IWeatherFetcher):
    base_url = "https://api.openweathermap.org/data/2.5"
    weather_method = f"{base_url}/weather"

    def __init__(self, config: OpenWeatherConfig, client: httpx.AsyncClient):
        self._api_key = config.openweather_api_key
        self._lang = config.openweather_lang
        self._units = config.openweather_units
        self._client = client

    async def fetch_weather(self, city: CityEnum) -> WeatherEntity | None:
        query = self._get_query_for_city(city)
        response = await self._client.get(self.weather_method, params=query)

        try:
            response_data = FetchWeatherData(**response.json())
            response.raise_for_status()
        except (ValidationError, HTTPStatusError):
            return None

        return WeatherEntity(
            temperature=response_data.main.temp,
            humidity=response_data.main.humidity,
            date=date.today(),
            city=city,
        )

    def _get_query_for_city(self, city: CityEnum) -> dict[str, str]:
        lat, lon = LAT_LONG_BY_CITY_MAPPING.get(city, (None, None))
        if not any((lat, lon)):
            raise NotImplemented(f"Необходимо определить координаты для города {city}")

        return {
            "lat": lat,
            "lon": lon,
            "appid": self._api_key,
            "lang": self._lang,
            "units": self._units,
        }
