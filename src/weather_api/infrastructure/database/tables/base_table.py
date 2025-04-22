from enum import Enum

from sqlalchemy import MetaData, SmallInteger, Numeric
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import DeclarativeBase

from weather_api.domain.types import CelsiusType, HumidityType


class Base(DeclarativeBase):

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )

    type_annotation_map = {
        Enum: postgresql.ENUM,
        CelsiusType: Numeric(precision=5, scale=2),
        HumidityType: SmallInteger,
    }
