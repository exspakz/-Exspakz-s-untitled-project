import telebot
from api import save_chat_id
from bot import settings


bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Please send me the token you\'ve received from our system.')


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    token = message.text
    chat_id = message.chat.id
    if save_chat_id(token, chat_id):
        bot.reply_to(message, 'Token is successfully linked with this chat.')
    else:
        bot.reply_to(message, 'Failed to link the token. Please make sure it\'s valid.')


if __name__ == '__main__':
    bot.polling(none_stop=True)
