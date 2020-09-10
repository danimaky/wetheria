from unittest.mock import patch
from weather.utils import fetch_information_from_weather_api, clean_weather_api_response
from requests.exceptions import RequestException
from freezegun import freeze_time
from weather.tests.constants import INFORMATION, EXPECTED_OUTPUT


@patch("weather.utils.requests.get")
def test_fetch_information_from_weather_api_ok_response(mock_get):
    """
    Testing function to get data from API endpoint in case of a good response
    :param mock_get: Mock for get function
    :return:
    """
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: INFORMATION
    response = fetch_information_from_weather_api("Bogota", "co")
    assert mock_get.called
    assert mock_get.call_count == 1
    assert response == INFORMATION


@patch("weather.utils.requests.get")
@patch("weather.utils.time.sleep")
def test_fetch_information_from_weather_api_connection_error_retry(mock_sleep, mock_get):
    """
    Testing function to get data from API endpoint in wrong response like timout
    we should do 3 retry
    :param mock_sleep: Mock for sleep function to avoid waits during testing process
    :param mock_get: Mock for get function
    :return:
    """
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
    """
    Testing function to clean raw data and validate the correct structure of it
    :param mock_get: Mock for get function
    :return:
    """
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: INFORMATION
    response = fetch_information_from_weather_api("Bogota", "co")
    cleaned_data = clean_weather_api_response(response)
    assert cleaned_data == EXPECTED_OUTPUT


@patch("weather.utils.requests.get")
def test_clean_weather_api_response_not_found(mock_get):
    """
    Testing function to clean raw data, in case of a wrong response we are going to reply
    same message to end user
    :param mock_get: Mock for get function
    :return:
    """
    information = {"cod": "404", "message": "city not found"}
    mock_get.return_value.status_code = 404
    mock_get.return_value.json = lambda: information
    response = fetch_information_from_weather_api("XXX", "ll")
    expected_output = {"message": "city not found"}
    cleaned_data = clean_weather_api_response(response)
    assert cleaned_data == expected_output
