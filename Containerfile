FROM python:3.11
WORKDIR /app
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN python -m venv venv
RUN bash ./venv/bin/activate
RUN pip install -r requirements.txt
COPY . .
RUN ./prepare.bash
CMD [ "pytest" ]
