FROM python:3.6-alpine

WORKDIR /home
COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY vizz_flask.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP vizz_flask.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]