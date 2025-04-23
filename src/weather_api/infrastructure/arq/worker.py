import asyncio
from typing import Sequence

from arq.connections import RedisSettings
from arq.cron import CronJob, cron
from arq.typing import StartupShutdown, WorkerCoroutine
from arq.worker import create_worker
from dishka import make_async_container
from dishka.integrations.arq import setup_dishka

from weather_api.config import Config
from weather_api.infrastructure.logging.setup_logging import setup_logging
from weather_api.main.ioc import AppProvider
from weather_api.presentation.cron import fetch_weather_cron, alert_missing_weather_data

config = Config()


class WorkerSettings:
    redis_settings: RedisSettings = RedisSettings(
        host=config.redis.redis_host,
        port=config.redis.redis_port,
        database=config.redis.redis_database,
    )

    allow_abort_jobs: bool = True
    on_startup: StartupShutdown | None = None
    on_shutdown: StartupShutdown | None = None

    functions: Sequence[WorkerCoroutine] = []

    cron_jobs: Sequence[CronJob] = [
        # Каждый день в 00:00 UTC
        cron(
            fetch_weather_cron,  # type: ignore # inject ломает тайпхинт у корутины
            hour=0,
            minute=0,
        ),
        # Каждый день в 01:00 UTC
        cron(
            alert_missing_weather_data,  # type: ignore
            hour=1,
            minute=0,
        ),
    ]


async def main():
    container = make_async_container(AppProvider(), context={Config: config})
    setup_logging(config.application.log_config_file)
    worker = create_worker(WorkerSettings)
    setup_dishka(container=container, worker_settings=worker)

    try:
        await worker.async_run()
    finally:
        await container.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except asyncio.CancelledError:
        pass
