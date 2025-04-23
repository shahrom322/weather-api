from weather_api.application.interfaces import IWeatherWriter, IWeatherFetcher
from weather_api.domain.enum import CityEnum
from weather_api.domain.exceptions import CantFetchDataError, CantSaveDataError


class FetchWeatherUseCase:

    def __init__(self, writer_gateway: IWeatherWriter, fetch_client: IWeatherFetcher):
        self._writer_gateway = writer_gateway
        self._fetch_client = fetch_client

    async def __call__(self) -> None:
        for city in CityEnum:

            weather_data = await self._fetch_client.fetch_weather(city)
            if weather_data is None:
                raise CantFetchDataError("Ошибка при попытке получить данные о погоде")

            weather_data = await self._writer_gateway.save_weather(weather_data)
            if weather_data is None:
                raise CantSaveDataError(
                    "Ошибка при попытке записать данные о погоде в хранилище"
                )

        await self._writer_gateway.commit()
