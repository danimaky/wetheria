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

try:
    exec(open(os.path.join(BASE_DIR, 'wetheria/settings_local.py')).read())
except IOError:
    raise Exception('error reading local settings')
