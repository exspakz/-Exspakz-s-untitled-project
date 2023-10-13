import logging
import os
from dotenv import load_dotenv

load_dotenv()

# Common settings

DEBUG = os.environ.get('DEBUG', default=False)
TOKEN = os.environ.get('TOKEN')
PROTOCOL = 'https' if not DEBUG else 'http'

API_DOMAIN_BASE = os.environ.get('API_DOMAIN', default='127.0.0.1:8000')
API_DOMAIN = f'{PROTOCOL}://{API_DOMAIN_BASE}'

# Logging settings

LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT)
