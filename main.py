import requests
import json
import time

def check_app_health(app_url):
    try:
        response = requests.get(app_url)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        return False

def send_slack_notification(slack_url, message):
    payload = {
        "text": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(slack_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        pass

if __name__ == "__main__":
    app_url = "<App_URL>"
    slack_url = "<Slack_URL>"
    while True:
        if not check_app_health(app_url):
            send_slack_notification(slack_url, "App is not healthy. Please Check!")
        time.sleep(60)