from prometheus_client import Gauge, generate_latest
from fastapi import FastAPI, Response
import requests

app = FastAPI()

# Define a Gauge metric with additional labels
HEALTH = Gauge(
  'sentry_health_status_code',
  'HTTP Status Code of the Health Check',
  ['method', 'endpoint']
)


def health_check():
  try:
    # Perform a GET request to your health check endpoint
    response = requests.get('http://nginx:80')
    return response.status_code
  except requests.RequestException:
    # Return a specific status code or 0 to indicate an error in making the request
    return 0


@app.get('/metrics')
async def metrics():
  # Update the gauge with the latest status code from health_check
  status_code = health_check()
  HEALTH.labels(method='GET', endpoint='/').set(status_code)
  return Response(content=generate_latest(), media_type="text/plain")
