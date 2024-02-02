FROM registry.docker.ir/python:3.11.4
WORKDIR /sentry
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0"]