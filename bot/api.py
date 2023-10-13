import logging

from requests import post
from requests.exceptions import ConnectionError

from .settings import API_DOMAIN

logger = logging.getLogger(__name__)

CHAT_ID = f'http://{API_DOMAIN}/telegram/chat_id/'


def save_chat_id(token, chat_id):
    headers = {'Content-Type': 'application/json'}
    data = {'token': token, 'chat_id': chat_id}
    try:
        response = post(CHAT_ID, json=data, headers=headers)
        if response.status_code == 200:
            logger.info(f'Successfully saved chat_id {chat_id} with token {token}')
            return True, None
        else:
            logger.warning(
                f'Failed to save chat_id {chat_id} with token {token}. '
                f'Status code: {response.status_code}'
            )
            return False, 'Failed to link the token. Please make sure it\'s valid.'
    except ConnectionError:
        logger.error(
            f'Failed to connect to the server when saving chat_id {chat_id} '
            f'with token {token}. Please check if the server is running.'
        )
        return False, 'Server is currently unreachable. Please try again later.'

