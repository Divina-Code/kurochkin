#!/usr/bin/env python3

import telebot

bot = telebot.TeleBot('1259165465:AAF0YRiXtF5Rn29H9VgRfELm366qBIb5oXM')

@bot.message_handler(content_types=['text'])
def ans_mess(message):
    print(message.chat.username)
    print(message)
    user = message.chat.username
    id = message.chat.id
    bot.send_message(id, f"Hello {user}, you write this - {message.text}") # message.text[::-1],

bot.polling() # забираем сообщение у бота