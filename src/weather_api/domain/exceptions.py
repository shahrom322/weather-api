class BaseError(Exception): ...


class InvalidDateRangeError(BaseError):
    """
    Исключение, возникающее при проверке дат диапазона
    """


class CantFetchDataError(BaseError):
    """
    Исключение, возникающее при попытке получить данные о погоде из стороннего API
    """


class CantSaveDataError(BaseError):
    """
    Исключение, возникающее при попытке записать данные о погоде в хранилище
    """
