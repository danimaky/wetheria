from unittest.mock import patch
from weather.utils import fetch_information_from_weather_api
from requests.exceptions import RequestException


@patch("weather.utils.requests.get")
def test_fetch_information_from_weather_api_well_response(mock_get):
    INFORMATION = {
        "coord": {
            "lon":-74.08,
            "lat":4.61
        },
        "weather":[
            {
                "id":802,
                "main":"Clouds",
                "description":"scattered clouds",
                "icon":"03n"
            }
        ],
        "base":"stations",
        "main":{
            "temp":283.15,
            "feels_like":282.21,
            "temp_min":283.15,
            "temp_max":283.15,
            "pressure":1027,
            "humidity":93
        },
        "visibility":10000,
        "wind":{
            "speed":1,
            "deg":0
        },
        "clouds":{
            "all":40
        },
        "dt":1599619177,
        "sys":{
            "type":1,
            "id":8582,
            "country":"CO",
            "sunrise":1599562134,
            "sunset":1599605947
        },
        "timezone":-18000,
        "id":3688689,
        "name":"Bogotá",
        "cod":200
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda : INFORMATION
    response = fetch_information_from_weather_api("Bogota", "co")
    assert mock_get.called
    assert mock_get.call_count == 1
    assert response == INFORMATION


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
