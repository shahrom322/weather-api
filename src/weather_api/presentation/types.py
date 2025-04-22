from enum import auto, StrEnum


class Tags(StrEnum):
    base = auto()


tags_metadata = [
    {
        "name": Tags.base,
        "description": "Базовые API сервиса",
    },
]
