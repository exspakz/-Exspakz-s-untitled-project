import os
from dotenv import load_dotenv

load_dotenv()


# Common settings

TOKEN = os.environ.get('TOKEN')
DOMAIN = os.environ.get('DOMAIN')
