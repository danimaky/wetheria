from unittest.mock import patch
from weather.utils import fetch_information_from_weather_api, clean_weather_api_response
from requests.exceptions import RequestException
from freezegun import freeze_time


@patch("weather.utils.requests.get")
def test_fetch_information_from_weather_api_ok_response(mock_get):
    information = {
        "coord": {
            "lon": -74.08,
            "lat": 4.61
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03n"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 283.15,
            "feels_like": 282.21,
            "temp_min": 283.15,
            "temp_max": 283.15,
            "pressure": 1027,
            "humidity": 93
        },
        "visibility": 10000,
        "wind": {
            "speed": 1,
            "deg": 0
        },
        "clouds": {
            "all": 40
        },
        "dt": 1599619177,
        "sys": {
            "type": 1,
            "id": 8582,
            "country": "CO",
            "sunrise": 1599562134,
            "sunset": 1599605947
        },
        "timezone": -18000,
        "id": 3688689,
        "name": "Bogotá",
        "cod": 200
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: information
    response = fetch_information_from_weather_api("Bogota", "co")
    assert mock_get.called
    assert mock_get.call_count == 1
    assert response == information


@patch("weather.utils.requests.get")
@patch("weather.utils.time.sleep")
def test_fetch_information_from_weather_api_connection_error_retry(mock_sleep, mock_get):
    exception_raised = False
    try:
        mock_get.side_effect = RequestException()
        fetch_information_from_weather_api("Bogota", "co",)
    except RequestException:
        exception_raised = True
    assert exception_raised
    assert mock_sleep
    assert mock_sleep.call_count == 2
    assert mock_get.called
    assert mock_get.call_count == 3


@freeze_time("2020-09-09 03:57:00", -5)
@patch("weather.utils.requests.get")
def test_clean_weather_api_response_ok(mock_get):
    information = {
        "coord": {
            "lon": -74.08,
            "lat": 4.61
        },
        "weather": [
            {
                "id": 802,
                "main": "Clouds",
                "description": "scattered clouds",
                "icon": "03n"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 283.15,
            "feels_like": 282.21,
            "temp_min": 283.15,
            "temp_max": 283.15,
            "pressure": 1027,
            "humidity": 93
        },
        "visibility": 10000,
        "wind": {
            "speed": 1,
            "deg": 0
        },
        "clouds": {
            "all": 40
        },
        "dt": 1599619177,
        "sys": {
            "type": 1,
            "id": 8582,
            "country": "CO",
            "sunrise": 1599562134,
            "sunset": 1599605947
        },
        "timezone": -18000,
        "id": 3688689,
        "name": "Bogotá",
        "cod": 200
    }
    expected_output = {
        "location_name": "Bogotá, CO",
        "temperature": "10 °C",
        "wind": {'deg': 0, 'speed': 1},
        "cloudines": "Scattered clouds",
        "presure": "1027 hpa",
        "humidity": "93%",
        "sunrise": "05:48",
        "sunset": "17:59",
        "geo_coordinates": "[4.61, -74.08]",
        "requested_time": "2020-09-08 22:57:00"
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: information
    response = fetch_information_from_weather_api("Bogota", "co")
    cleaned_data = clean_weather_api_response(response)
    assert cleaned_data == expected_output


@patch("weather.utils.requests.get")
def test_clean_weather_api_response_not_found(mock_get):
    information = {"cod": "404", "message": "city not found"}
    mock_get.return_value.status_code = 404
    mock_get.return_value.json = lambda: information
    response = fetch_information_from_weather_api("XXX", "ll")
    expected_output = {"message": "city not found"}
    cleaned_data = clean_weather_api_response(response)
    assert cleaned_data == expected_output
