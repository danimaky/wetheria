from freezegun import freeze_time
from unittest.mock import patch
from weather.tests.constants import INFORMATION, EXPECTED_OUTPUT
from time import sleep


def test_weather_api_malformed_request(client, ):
    """
    Testing endpoint validation to malformed requests
    :param client: Fixture for a client to fake flask App instance
    :return:
    """
    assert client.get("/weather").status_code == 400
    assert client.get("/weather?city=Bogota").status_code == 400
    assert client.get("/weather?country=co").status_code == 400
    assert client.get("/weather?city=Bogota&country=c,").status_code == 400
    assert client.get("/weather?city=Bogota&country=c2").status_code == 400
    assert client.get("/weather?city=Bogota&country=c").status_code == 400


@freeze_time("2020-09-09 03:57:00", -5)
@patch("weather.utils.requests.get")
def test_weather_api_correct_request(mock_get, client):
    """
    Testing endpoint response for success case
    :param mock_get: Mock for get function
    :param client: Fixture for a client to fake flask App instance
    :return:
    """
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: INFORMATION
    request = client.get("/weather?city=Bogota&country=co")
    assert request.status_code == 200
    assert request.get_json() == EXPECTED_OUTPUT


@patch("weather.utils.requests.get")
def test_weather_api_cached_request(mock_get, client):
    """
    Testing endpoint cache functionality
    :param mock_get: Mock for get function
    :param client: Fixture for a client to fake flask App instance
    :return:
    """
    mock_get.return_value.status_code = 200
    mock_get.return_value.json = lambda: INFORMATION
    request = client.get("/weather?city=Bogota&country=co")
    assert request.status_code == 200
    first_response = request.get_json()
    sleep(1)
    request = client.get("/weather?city=Bogota&country=co")
    assert request.status_code == 200
    second_response = request.get_json()
    assert first_response == second_response
