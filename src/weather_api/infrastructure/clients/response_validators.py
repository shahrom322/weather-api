from pydantic import BaseModel

from weather_api.domain.types import CelsiusType, HumidityType


class MainWeatherData(BaseModel):
    temp: CelsiusType
    humidity: HumidityType


class FetchWeatherData(BaseModel):
    main: MainWeatherData
