"""
    Application configuration.
"""
import os

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)

# load environment in env variable

ENV = "production"
DEBUG = False

SECRET_KEY = '|iWYCOt6G^[Zt&ov|PD+@RRI^ae-2R^8S}6QI4=$lNORV+||vm-3qA,qApSOP|(H'
CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
WEATHER_API_TOKEN = "1508a9a4840a5574c822d70ca2132032"

try:
    exec(open(os.path.join(BASE_DIR, 'wetheria/settings_local.py')).read())
except IOError:
    raise Exception('error reading local settings')
