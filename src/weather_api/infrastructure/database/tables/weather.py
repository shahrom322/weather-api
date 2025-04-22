from sqlalchemy import Index
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from weather_api.domain.entities.weather import WeatherEntity
from weather_api.domain.enum import CityEnum
from weather_api.domain.types import CelsiusType, HumidityType
from weather_api.infrastructure.database.tables.base_table import Base


class WeatherModel(Base):
    __tablename__ = "weather"
    __table_args__ = (
        # композитный индекс для запросов по городу + диапазону дат
        Index("idx_weather_city_date", "city", "date"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city: Mapped[CityEnum]
    date: Mapped[date]
    temperature: Mapped[CelsiusType]
    humidity: Mapped[HumidityType]

    def to_entity(self) -> WeatherEntity:
        return WeatherEntity(
            city=self.city,
            date=self.date,
            temperature=self.temperature,
            humidity=self.humidity,
        )
