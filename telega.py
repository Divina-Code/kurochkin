#!/usr/bin/env python3

import telebot
from random import randint as rid

bot = telebot.TeleBot('1259165465:AAF0YRiXtF5Rn29H9VgRfELm366qBIb5oXM')

# mods

@bot.message_handler(content_types=['text'])
def ans_mess(message):
    mes = message.text
    user = message.chat.username
    id = message.chat.id
    bot.send_message(id, "Enter some word")
    # bot.send_message(id, f"Hello {user}, you write this - {message.text}") # message.text[::-1]
    inp = message.text.lower().split()
    for word in inp:
        if word[::-1] == word:
            bot.send_message(id, "that word is polindrom")
        else:
            bot.send_message(id, "that word isn`t polindrom")


bot.polling() # забираем сообщение у бота