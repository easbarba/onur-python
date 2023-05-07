FROM python:3.11
WORKDIR /app
RUN pip install --upgrade pip poetry
COPY ./poetry.lock ./pyproject.toml .
RUN poetry install
COPY . .
RUN ./prepare.bash
CMD ["poetry", "run", "pytest"]
