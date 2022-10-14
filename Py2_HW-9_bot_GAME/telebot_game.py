# pip install pyTelegramBotAPI

import telebot
from telebot import types
from tok import token
from random import randint


client = telebot.TeleBot(token)
secret_data = randint(0,10)

@client.message_handler(commands=['start'])
def start(message):
    client.send_message(message.chat.id, 'Игра "угадай число". \n'
                                               'Начало - /go \n'
                                               'Правила - /info \n')

@client.message_handler(commands=['info'])
def info(message):
    rmk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rmk.add(types.KeyboardButton("Да"), types.KeyboardButton("Нет"))
    msg = client.send_message(message.chat.id, 'Я буду закадывать число от 0 до 10 \n'
                                               'Ты - вводить числа пока не угадаешь \n'
                                               'Поиграем? ', reply_markup=rmk)
    client.register_next_step_handler(msg, steps)

@client.message_handler(commands=['go'])
def info(message):
    rmk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rmk.add(types.KeyboardButton("Да"), types.KeyboardButton("Нет"))
    msg = client.send_message(message.chat.id, 'Погнали?', reply_markup=rmk)
    client.register_next_step_handler(msg, steps)


def steps(message):
    global secret_data
    if message.text == "Да":
        msg = client.send_message(message.chat.id, 'Я загадал число от 0 до 10.\n'
                                                   'Введи число.')
        client.register_next_step_handler(msg, steps)
    elif message.text == "Нет":
        # msg = client.register_next_step_handler(exit_1)
        client.send_message(message.chat.id, 'Ну нет, так - нет. До свидания.')
    elif message.text == str(secret_data):
        msg = client.send_message(message.chat.id, f'Круто - угадал. Было загадано {secret_data}')
        # client.register_next_step_handler(msg, exit_2)
    elif message.text <= str(secret_data):
        msg = client.send_message(message.chat.id, f'Нет. Введи по-БОЛЬШЕ. ')
        client.register_next_step_handler(msg, steps)
    elif message.text >= str(secret_data):
        msg = client.send_message(message.chat.id, f'Нет. Введи по-МЕНЬШЕ')
        client.register_next_step_handler(msg, steps)

client.polling()
