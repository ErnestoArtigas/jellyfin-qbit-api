FROM python:3.13-alpine AS build-stage

ENV POETRY_VERSION=2.1.2

WORKDIR /app

COPY ./pyproject.toml /app/pyproject.toml
COPY ./poetry.lock /app/poetry.lock

RUN pip install "poetry==$POETRY_VERSION" \
    && poetry install --no-root --no-ansi --no-interaction \
    && poetry export -f requirements.txt -o requirements.txt

FROM python:3.13-alpine AS prod-stage

WORKDIR /app

COPY --from=build-stage /app/requirements.txt .

RUN pip install -r requirements.txt

COPY /app /app/app

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py", "--proxy-headers", "--port", "8000"]
