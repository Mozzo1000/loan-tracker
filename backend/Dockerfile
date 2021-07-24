# syntax=docker/dockerfile:1
FROM python:3
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
COPY requirements-api.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY ./api .
CMD ["flask", "run"]