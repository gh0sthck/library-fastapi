FROM python:3.12.2-alpine3.19

ENV PYTHONBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.8.2 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' 

WORKDIR /library/

COPY . /library/

RUN pip install poetry
RUN poetry install --no-root --no-interaction --no-ansi

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "--host", "0.0.0.0", "--port", "8000", "--reload" ]
CMD [ "main:app" ]
