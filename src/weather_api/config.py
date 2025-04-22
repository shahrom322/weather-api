from pathlib import Path

from pydantic_settings import BaseSettings
from sqlalchemy.engine.interfaces import IsolationLevel

PROJECT_DIR = Path(__file__).parent.parent.parent


class BaseConfig(BaseSettings):

    class Config:
        env_file = PROJECT_DIR / ".env"


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
