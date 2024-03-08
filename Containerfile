FROM python:3.12

WORKDIR /app
RUN pip install --upgrade pip

COPY ./pyproject.toml .
RUN python -m venv venv
RUN bash ./venv/bin/activate
RUN pip install .

COPY . .
RUN ./prepare.bash

CMD [ "pytest" ]
