FROM python:slim-bullseye as dependencies
ARG APP_DIR=weather_app

RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

COPY ./requirements.txt ./
RUN python3 -m venv env && . env/bin/activate
RUN pip3 install -r requirements.txt
ADD src src

CMD python3 src/main.py