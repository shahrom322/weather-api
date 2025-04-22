class BaseError(Exception): ...


class InvalidDateRangeError(BaseError):
    """
    Исключение, возникающее при проверке дат диапазона
    """
