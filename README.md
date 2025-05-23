# Weather API service

Микросервис для сбора, хранения и анализа данных о погоде

## Стек

- Python 3.12
- FastAPI
- SQLAlchemy 2.0 + asyncpg
- PostgreSQL
- ARQ (отложенные задачи)
- dishka (IoC-контейнер)
- Redis (бэкэнд для ARQ)
- Docker, Docker Compose

## Полученный результат

- Миграции и модели SQLAlchemy 2.0 для PostgreSQL
- Отложенные задачи при помощи ARQ
- Регулярный сбор данных
- Регулярная проверка свежести данных
- FastAPI-приложение с двумя эндпоинтами и Swagger-документацией
- IoC-контейнер dishka для конфигурации и зависимостей

## Установка и запуск
1. Скопировать шаблон .env и заполнить переменные
2. Собрать и запустить контейнеры `docker-compose up --build`