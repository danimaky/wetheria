INFORMATION = {
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

EXPECTED_OUTPUT = {
        "location_name": "Bogota, CO",
        "temperature": "10 C",
        "wind": {'deg': 0, 'speed': 1},
        "cloudines": "Scattered clouds",
        "presure": "1027 hpa",
        "humidity": "93%",
        "sunrise": "05:48",
        "sunset": "17:59",
        "geo_coordinates": "[4.61, -74.08]",
        "requested_time": "2020-09-08 22:57:00"
    }
