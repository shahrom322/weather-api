from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings
from sqlalchemy.engine.interfaces import IsolationLevel

PROJECT_DIR = Path(__file__).parent.parent.parent


class BaseConfig(BaseSettings):

    class Config:
        env_file = PROJECT_DIR / ".env"
        extra = "ignore"


class PostgresConfig(BaseConfig):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    max_overflow: int = 30
    pool_size: int = 30
    pool_recycle: int = 3600
    isolation_level: IsolationLevel = "READ COMMITTED"

    @property
    def uri(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@"
            f"{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


class OpenWeatherConfig(BaseConfig):
    openweather_api_key: str
    openweather_lang: str = "en"
    openweather_units: str = "metric"


class RedisConfig(BaseConfig):
    redis_host: str
    redis_port: int
    redis_database: int


class AppConfig(BaseConfig):
    app_name: str = "weather_api"
    log_config_file: Path = (
        PROJECT_DIR
        / "src"
        / "weather_api"
        / "infrastructure"
        / "logging"
        / "log_config.json"
    )


class Config(BaseConfig):
    postgres: PostgresConfig = Field(default_factory=PostgresConfig)
    application: AppConfig = Field(default_factory=AppConfig)
    openweather: OpenWeatherConfig = Field(default_factory=OpenWeatherConfig)
    redis: RedisConfig = Field(default_factory=RedisConfig)
