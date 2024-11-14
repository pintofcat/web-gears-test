FROM python:3.10-slim as builder

ARG ENVIRONMENT

ENV ENVIRONMENT=$ENVIRONMENT \
    IM_VERSION=$IM_VERSION \
    IM_COMMIT_HASH=$IM_COMMIT_HASH \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.poetry/bin:$PATH" \
    POETRY_VERSION=1.8.2

RUN apt-get update && \
    apt-get install -y --no-install-recommends git curl && \
    rm -rf /var/lib/apt/lists/ \
    apt-get clean;

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN pip install --upgrade pip

RUN curl -sSL "https://install.python-poetry.org" | POETRY_HOME="/root/.poetry/" python - --version $POETRY_VERSION; \
    poetry config virtualenvs.create false \
    && poetry export \
        --format requirements.txt \
        --output requirements.txt \
        --without-hashes \
        --with-credentials \
        $(test "$ENVIRONMENT" = "dev" && echo "--dev") \
    && mkdir /wheels \
    && pip wheel -r requirements.txt --wheel-dir /wheels \
    && rm requirements.txt


FROM python:3.10.4-slim-buster

ENV PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_INDEX=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

WORKDIR /code

COPY --from=builder /wheels /wheels
COPY . /code
RUN pip install /wheels/*


ENTRYPOINT ["/code/entrypoint.sh"]
