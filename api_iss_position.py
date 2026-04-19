import requests

url = "http://api.open-notify.org/iss-now.json"


# Takes a url, requests and expects a json response
def fetch_json(url: str):
    r = requests.get(url)
    # Given that statuscode is 200, convert response from json to dict
    if r.status_code == 200:
        return r.json()
    else:
        return None


# Calls fetch_json, if response is not None, normalize data and return it
def get_iss_position():
    data = fetch_json(url)
    if data is not None:
        # Changes datatype of values to float
        parsed_data = {
            "latitude": float(data["iss_position"]["latitude"]),
            "longitude": float(data["iss_position"]["longitude"]),
        }
        return parsed_data
