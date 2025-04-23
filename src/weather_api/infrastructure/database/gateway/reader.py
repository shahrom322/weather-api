from datetime import date

from sqlalchemy import select, exists

from weather_api.application.interfaces import IWeatherReader
from weather_api.domain.dto import GetWeatherListDTO
from weather_api.domain.entities.weather import WeatherEntity
from weather_api.infrastructure.database.gateway.base import BaseGateway
from weather_api.infrastructure.database.tables import WeatherModel


class WeatherDataReader(BaseGateway, IWeatherReader):

    async def get_weather_list(self, dto: GetWeatherListDTO) -> list[WeatherEntity]:
        stmt = select(WeatherModel).where(
            dto.city == WeatherModel.city,
            WeatherModel.date.between(dto.start_date, dto.end_date),
        )

        result = (await self._session.scalars(stmt)).all()
        return [model.to_entity() for model in result]

    async def is_weather_data_exists(self, target_day: date) -> bool:
        stmt = select(exists().where(target_day == WeatherModel.date))
        return await self._session.scalar(stmt)
