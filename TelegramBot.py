import requests
import json
import telebot
from hidden_data import discrod_authorization, telegram_bot_token, channel_id

def discord_channel_messages(channel_id):
    headers = {
        'authorization': discrod_authorization
    }
    req = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)
    json_file = json.loads(req.text)
    for value in json_file:
        result = value['content']
        return result

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Hi, that`s the last channel message:')
        send_text(message)

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        bot.send_message(message.chat.id, discord_channel_messages(channel_id))

    bot.polling(none_stop=True)

telegram_bot(telegram_bot_token)
