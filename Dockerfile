FROM python:slim-bullseye as dependencies
ARG APP_DIR=py_weather_app
EXPOSE 8000

RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

COPY ./requirements.txt ./
RUN python3 -m venv env && . env/bin/activate
RUN pip3 install -r requirements.txt
ADD src src

CMD uvicorn src.main:app --host 0.0.0.0