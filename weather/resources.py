from flask_restful import Resource, reqparse
from flask import make_response
from wetheria.extensions import api, cache
from weather.utils import fetch_information_from_weather_api, clean_weather_api_response, validate_country


class WeatherApiView(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    @cache.cached(timeout=120, query_string=True)
    def get(self):
        fields = [
            {
                "name": "city",
                "location": "values",
                "required": True,
                "default": "",
                "type": str,
            },
            {
                "name": "country",
                "location": "values",
                "required": True,
                "default": "",
                "type": validate_country,
            },
        ]
        [self.parser.add_argument(**x) for x in fields]
        args = self.parser.parse_args()
        raw_data = fetch_information_from_weather_api(city=args['city'], country_code=args['country'])
        cleaned_data = clean_weather_api_response(raw_data=raw_data)
        return cleaned_data, raw_data['cod']


class ErrorApiView(Resource):

    def get(self):
        value = "a" + 1
        return make_response({}, 200)


api.add_resource(WeatherApiView, "/weather")
api.add_resource(ErrorApiView, "/500")
