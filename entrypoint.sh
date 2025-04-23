#!/bin/bash

# Включение прерывания в случае ошибки в команде
set -e
export PYTHONPATH=./src/


if [ "${1}" == "bash" ]; then
    # Выполнение команды bash
    exec "$@"
elif [ "${1}" == "rq_worker" ]; then
    # Запуск воркера для выполнения фоновых задач
    exec python ./src/weather_api/infrastructure/arq/worker.py
else
    # Запуск web приложения
    alembic upgrade heads
    exec uvicorn --factory src.weather_api.main.web:create_app \
    --host 0.0.0.0 \
    --log-config ./src/weather_api/infrastructure/logging/log_config.json
fi