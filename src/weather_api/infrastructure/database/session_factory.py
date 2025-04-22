from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine

from weather_api.config import PostgresConfig


def get_session_maker(psql_config: PostgresConfig) -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(
        psql_config.uri,
        max_overflow=psql_config.max_overflow,
        pool_size=psql_config.pool_size,
        pool_recycle=psql_config.pool_recycle,
        isolation_level=psql_config.isolation_level,
    )
    return async_sessionmaker(engine, class_=AsyncSession)
