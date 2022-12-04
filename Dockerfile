FROM python:3.6-slim

ENV FLASK_APP=backEnd_1

ENV FLASK_DEBUG=$FLASK_DEBUG

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY backEnd_1 /opt/backEnd_1

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT
