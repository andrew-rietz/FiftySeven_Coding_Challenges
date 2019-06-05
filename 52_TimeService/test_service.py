import requests
import json


def main():
    api_resp = requests.get("http://127.0.0.1:5000/current-time")
    if api_resp.status_code != 200:
        print(f"Error accessing API (Status code {api_resp.status_code})")
    else:
        js = api_resp.json()
        current_time = js["currentTime"]

        print(
            "Success!\n"
            + f"The current time (in UTC) is {current_time}\n"
            + f"The server is {api_resp.headers['server']}\n"
            + f"The content type is {api_resp.headers['content-type']}"
        )


main()
