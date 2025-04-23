from weather_api.application.interfaces import IWeatherWriter
from weather_api.domain.entities.weather import WeatherEntity
from weather_api.infrastructure.database.gateway.base import BaseGateway
from weather_api.infrastructure.database.tables import WeatherModel


class WeatherDataWriter(BaseGateway, IWeatherWriter):

    async def save_weather(self, weather: WeatherEntity) -> WeatherEntity | None:
        db_model = WeatherModel.from_entity(weather)
        self._session.add(db_model)
        await self._session.flush()
        await self._session.refresh(db_model)
        return db_model.to_entity()

    async def commit(self) -> None:
        await self._session.commit()
