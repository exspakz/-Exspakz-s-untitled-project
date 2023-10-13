from requests import post
from .settings import DOMAIN

CHAT_ID = f'http://{DOMAIN}/telegram/chat_id/'


def save_chat_id(token, chat_id):
    headers = {'Content-Type': 'application/json'}
    data = {'token': token, 'chat_id': chat_id}
    response = post(CHAT_ID, json=data, headers=headers)
    return response.status_code == 200
