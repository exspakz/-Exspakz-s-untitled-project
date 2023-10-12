from requests import post
from bot import settings


def save_chat_id(token, chat_id):
    headers = {'Content-Type': 'application/json'}
    data = {'token': token, 'chat_id': chat_id}
    response = post(settings.CHAT_ID, json=data, headers=headers)
    return response.status_code == 200
