import requests
from datetime import datetime, timedelta
def call_fastapi_endpoint():
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=1)
    url = "http://51.89.116.169/get_data"
    payload = {
    "start_date": start_date.strftime('%Y-%m-%d'),
    "end_date": end_date.strftime('%Y-%m-%d')
}

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Failed:", response.status_code, response.text)

if __name__ == "__main__":
    call_fastapi_endpoint()
