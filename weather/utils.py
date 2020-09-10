from wetheria.settings import WEATHER_API_URL, WEATHER_API_TOKEN
import time
import requests
import datetime


def fetch_information_from_weather_api(city: str, country_code: str, retry: int = 1):
    """
    Function to fetch information from Weather API in base of an specific query
    :param city: Name of city to look up
    :param country_code: Country code to look up, this should be a two characters string
    :param retry: Number of retry, this is used for fetching retries.
    :return: Dict Structure obtained from endpoint
    """
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


def clean_weather_api_response(raw_data: dict = dict()):
    """
    Function to clean raw data obtained from API endpoint.
    :param raw_data: A dictionary structure
    :return: It's a dictionary human-readable
    """
    cleaned_data = {}
    if raw_data['cod'] == 200:
        temperature = raw_data['main']['temp']
        temperature = int(temperature - 273.15)
        cleaned_data = {
            "location_name": f"{raw_data.get('name', 'N/A')}, {raw_data.get('sys', {}).get('country')}",
            "temperature": f"{temperature} °C",
            "wind": raw_data["wind"],
            "cloudines": raw_data["weather"][0]["description"].capitalize(),
            "presure": f"{raw_data['main']['pressure']} hpa",
            "humidity": f"{raw_data['main']['humidity']}%",
            "sunrise": f"{datetime.datetime.fromtimestamp(raw_data['sys']['sunrise']).strftime('%H:%M')}",
            "sunset": f"{datetime.datetime.fromtimestamp(raw_data['sys']['sunset']).strftime('%H:%M')}",
            "geo_coordinates": f"[{raw_data['coord']['lat']}, {raw_data['coord']['lon']}]",
            "requested_time": f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        }
    else:
        cleaned_data['message'] = raw_data['message']
    return cleaned_data
