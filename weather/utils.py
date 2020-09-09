from wetheria.settings import WEATHER_API_URL, WEATHER_API_TOKEN
import time
import requests


def fetch_information_from_weather_api(city, country_code, retry=1):
    params = {
        "q": f"{city},{country_code}",
        "appid": WEATHER_API_TOKEN
    }
    try:
        response = requests.get(WEATHER_API_URL, params=params)
    except requests.exceptions.RequestException as e:
        if retry < 3:
            time.sleep(1 * retry)
            return fetch_information_from_weather_api(city, country_code, retry=retry+1,)
        else:
            raise e
    return response.json()
