from decimal import Decimal

from weather_api.application.interfaces import IWeatherReader
from weather_api.domain.dto import GetWeatherListDTO, StatsDTO
from weather_api.domain.types import CelsiusType, HumidityType
from weather_api.domain.utils import validate_date_range


class GetStatsUseCase:

    def __init__(self, reader_gateway: IWeatherReader):
        self._reader_gateway = reader_gateway

    async def __call__(self, dto: GetWeatherListDTO) -> StatsDTO:
        validate_date_range(dto.start_date, dto.end_date)

        data = await self._reader_gateway.get_weather_list(dto)

        if (count := len(data)) == 0:
            return StatsDTO(
                avg_temperature=CelsiusType(Decimal(0)), avg_humidity=HumidityType(0)
            )

        # Бизнес‑логика агрегации выполняется здесь, а не в слое доступа к данным,
        # чтобы именно у use‑case оставалась ответственность за все правила обработки и трансформации данных.

        # В угоду оптимизации агрегированные данные можно получить сразу из БД,
        # но тут я решил следовать принципам чистой архитектуры.
        total_temp = sum(record.temperature for record in data)
        total_hum = sum(record.humidity for record in data)

        avg_temp = CelsiusType(Decimal(round(total_temp / count, 2)))
        avg_humidity = HumidityType(int(total_hum / count))

        return StatsDTO(avg_temperature=avg_temp, avg_humidity=avg_humidity)
