import logging
import os
from dotenv import load_dotenv

load_dotenv()


# Common settings

TOKEN = os.environ.get('TOKEN')
DOMAIN = os.environ.get('DOMAIN', default='127.0.0.1:8000')


# Logging settings

LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT)
