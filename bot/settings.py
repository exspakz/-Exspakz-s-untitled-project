import os
from dotenv import load_dotenv

load_dotenv()


# Common settings

TOKEN = os.environ.get('TOKEN')
DOMAIN = os.environ.get('DOMAIN')


# API endpoints

CHAT_ID = f'http://{DOMAIN}/telegram/chat_id/'
