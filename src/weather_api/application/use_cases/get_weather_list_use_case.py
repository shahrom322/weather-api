from weather_api.application.interfaces import IWeatherReader
from weather_api.domain.dto import GetWeatherListDTO, ListWeatherDTO


class GetWeatherListUseCase:

    def __init__(self, reader_gateway: IWeatherReader):
        self._reader_gateway = reader_gateway

    async def __call__(self, dto: GetWeatherListDTO) -> ListWeatherDTO:
        data = await self._reader_gateway.get_weather_list(dto)
        return ListWeatherDTO(data)
