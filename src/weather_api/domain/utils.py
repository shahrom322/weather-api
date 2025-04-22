from datetime import date

from weather_api.domain.exceptions import InvalidDateRangeError


def validate_date_range(start_date: date, end_date: date) -> None:
    if start_date > end_date:
        raise InvalidDateRangeError(
            "Дата начала диапазона не может быть позже, чем дата окончания"
        )
