import requests

url = "http://api.open-notify.org/astros.json"


# Takes a url as string, requests and expects a json response
def fetch_json(url: str):
    r = requests.get(url)
    # Given that statuscode is 200, convert response from json to dict
    if r.status_code == 200:
        # Converts to dictionary and returns
        return r.json()
    else:
        # If response is bad, print status code and return None
        print(f"Status code {r.status_code}. Expects 200")
        return None


# Calls fetch_json, if response is not None, normalize data and return it
def get_astronauts():
    data = fetch_json(url)
    if data is not None:
        parsed_data = {}
        parsed_data["number"] = data["number"]
        parsed_data["people"] = data["people"]
        return parsed_data
