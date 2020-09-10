from flask_restful import Resource, reqparse
from wetheria.extensions import api, cache
from weather.utils import fetch_information_from_weather_api, clean_weather_api_response
import re


class WeatherApiView(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

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
                "type": str,
            },
        ]
        [self.parser.add_argument(**x) for x in fields]
        args = self.parser.parse_args()
        if not len(args.get('country', '')) == 2 or re.search(r"\W|\d+", args.get('country', '')):
            return {
                "message": {
                    "country": "Country code should be an string composed by 2 character in lowercase"
                }
            }, 400
        raw_data = fetch_information_from_weather_api(city=args['city'], country_code=args['country'])
        cleaned_data = clean_weather_api_response(raw_data=raw_data)
        return cleaned_data


api.add_resource(WeatherApiView, "/weather")
