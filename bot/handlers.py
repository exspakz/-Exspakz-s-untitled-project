import logging
import time
import telebot

from bot.api import save_chat_id
from bot.settings import TOKEN


logger = logging.getLogger(__name__)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, 'Please send me the token you\'ve received from our system.'
    )
    logger.info(f'Sent welcome message to chat_id {message.chat.id}')


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    token = message.text
    chat_id = message.chat.id
    success, error_message = save_chat_id(token, chat_id)
    if success:
        bot.reply_to(message, 'Token is successfully linked with this chat.')
    else:
        bot.reply_to(message, error_message)


if __name__ == '__main__':
    while True:
        try:
            logger.info('Starting bot polling...')
            bot.polling(none_stop=True)
        except Exception as e:
            logger.error(f'Bot polling failed: {e}')
            time.sleep(15)
