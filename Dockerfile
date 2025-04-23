FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=2.1.1

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /opt/app/

COPY pyproject.toml /opt/app

RUN pip install setuptools && \
    poetry config virtualenvs.create false &&  \
    poetry install --only main --no-interaction --no-ansi --no-root -vv

COPY . /opt/app

ENTRYPOINT ["./entrypoint.sh"]
