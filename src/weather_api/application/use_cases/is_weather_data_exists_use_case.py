from datetime import date

from weather_api.application.interfaces import IWeatherReader


class IsWeatherDataExistsUseCase:

    def __init__(self, reader_gateway: IWeatherReader):
        self._reader_gateway = reader_gateway

    async def __call__(self) -> bool:
        return await self._reader_gateway.is_weather_data_exists(date.today())
