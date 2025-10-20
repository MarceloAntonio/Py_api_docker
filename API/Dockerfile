FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=api.py

ENV FLASK_RUN_HOST=0.0.0.0

ENV FLASK_DEBUG=1

CMD [ "flask", "run" ]