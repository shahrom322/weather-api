#!/bin/bash

# Включение прерывания в случае ошибки в команде
set -e
export PYTHONPATH=./src/


if [ "${1}" == "bash" ]; then
    # Выполнение команды bash
    exec "$@"
else
    # Запуск web приложения
    alembic upgrade heads
    exec uvicorn --factory src.weather_api.main.web:create_app
fi