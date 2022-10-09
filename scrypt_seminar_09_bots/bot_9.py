#!/usr/bin/env python
# pip install python-telegram-bot==v13.14

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler
from random import randint
from tok import token

bot_token = token
bot = Bot(bot_token)
updater = Updater(bot_token,  use_context=True)
dispatcher = updater.dispatcher

def start(update, content):
    content.bot.send_message(update.effective_chat.id, "Салют!")


def info(update, content):
    content.bot.send_message(update.effective_chat.id, "Это - бот!")


def roll(update, content):
    content.bot.send_message(update.effective_chat.id, text=str(randint(0,10)))

start_heandler = CommandHandler('start', start)
info_heandler = CommandHandler('info', info)
roll_heandler = CommandHandler('roll', roll)


dispatcher.add_handler(start_heandler)
dispatcher.add_handler(info_heandler)
dispatcher.add_handler(roll_heandler)

# ----- запускает цикл приема и обработки сообщений ----
updater.start_polling()
# ----- ждет завершения приложения -----
updater.idle()