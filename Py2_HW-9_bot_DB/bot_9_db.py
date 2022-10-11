# import data_base
import sqlite3

import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from tok import token_db

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )
#
# logger = logging.getLogger(__name__)

id_number = 0

def start(update, content):
    content.bot.send_message(update.effective_chat.id, "Привет. Я - бот-БД!\n"
                                                       "я буду  \n"
                                                       "открывать все данные    /open \n"
                                                       "удалять запись          /delete \n"
                                                       "добавлять запись        /insert \n"
                                                       "вносить изменения       /edit \n"
                                                       "искать нужную запись /find \n"
                                                       "выход по команде /stop")


def open(update, content):
    content.bot.send_message(update.effective_chat.id, "Это - open!")
    conn = sqlite3.connect('zavodd.db')
    cursor = conn.cursor()
    cursor.execute('select * from shtat')
    result = cursor.fetchall()
    print(result)
    content.bot.send_message(update.effective_chat.id, result)
    conn.close()
    # output_all()

def delete(update, content):
    content.bot.send_message(update.effective_chat.id, "Это - delete! Введите номер записи, которую дропнем")
    return 1

def execute_delete(update, content):
    id_number = int(update.message.text)
    print(id_number)
    content.bot.send_message(update.effective_chat.id, f'Ты выбрал {id_number}-ю запись')
    conn = sqlite3.connect('zavodd.db')
    cursor = conn.cursor()
    cursor.execute(f"delete from shtat where id = {id_number}");
    conn.commit()


def edit(update, content):
    content.bot.send_message(update.effective_chat.id, "Это - edit! Введи номер редактируемой записи")
    return 1

def execute_edit_id(update, content):
    global id_number
    id_number = int(update.message.text)
    # print(id_number)
    content.bot.send_message(update.effective_chat.id, f'Ты выбрал {id_number}-ю запись для редактирования')
    content.bot.send_message(update.effective_chat.id, f'Введи через пробел: ФАМИЛИЮ ТЕЛЕФ ДОЛЖНОСТЬ')
    return 2

def execute_edit_data(update, content):
    global id_number
    conn = sqlite3.connect('zavodd.db')
    cursor = conn.cursor()
    edit_data = (update.message.text)
    print(edit_data)
    name_ = edit_data.split()[0]
    tel_ = edit_data.split()[1]
    prof_ = edit_data.split()[2]
    cursor.execute(
                   f"update shtat set name = '{name_}', tel = '{tel_}', prof = '{prof_}' where id = {id_number}"
                   )
    conn.commit()

def insert(update, content):
    content.bot.send_message(update.effective_chat.id, "Это - insert!\n"
                                                       "Введи через пробел: ФАМИЛИЮ ТЕЛЕФ ДОЛЖНОСТЬ ")
    return 1

def execute_insert(update, content):

    conn = sqlite3.connect('zavodd.db')
    cursor = conn.cursor()
    insert_data = (update.message.text)
    print(insert_data)
    name_ = insert_data.split()[0]
    tel_ = insert_data.split()[1]
    prof_ = insert_data.split()[2]
    cursor.execute(f"insert into shtat (name,tel,prof) values ('{name_}','{tel_}','{prof_}')");
    conn.commit()


def find(update, content):
    content.bot.send_message(update.effective_chat.id, "Это - find!\n"
                                                       "Введи кусок имени для поиска")
    return 1


def execute_find(update, content):
    conn = sqlite3.connect('zavodd.db')
    cursor = conn.cursor()
    find_name = (update.message.text)
    print(find_name)
    cursor.execute(f'select * from shtat  where name like "%{find_name}%"')
    result = cursor.fetchall()
    print(result)
    content.bot.send_message(update.effective_chat.id, result)


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    context.bot.send_message(update.effective_chat.id, "Всего доброго")
    return ConversationHandler.END




bot_token = token_db
bot = Bot(bot_token)
updater = Updater(bot_token,  use_context=True)
dispatcher = updater.dispatcher

# ------ чтение из бота данных ---------------
    #---- выбор запси, которую дропаем -------
delete_records = ConversationHandler(
        entry_points=[CommandHandler('delete', delete)],
        states={
             # Функция считывает номер записи, которую мы хотим ДРОПНУТЬ
            1: [MessageHandler(Filters.text & ~Filters.command, execute_delete)] },
        fallbacks=[CommandHandler('stop', stop)]
                                    )

    #---- выбор запси, которую редактируем -------
edit_records = ConversationHandler(
        entry_points=[CommandHandler('edit', edit)],
        states={
               # Функция считывает номер записи, которую мы хотим РЕДАКТИРОВАТЬ
            1: [MessageHandler(Filters.text & ~Filters.command, execute_edit_id)],
                # Функция считывает ФИО ТЕЛ ДОЛЖНОСТЬ
            2: [MessageHandler(Filters.text & ~Filters.command, execute_edit_data)] },
        fallbacks=[CommandHandler('stop', stop)]
                                    )
    #---- НОВАЯ запись--------------
new_records = ConversationHandler(
        entry_points=[CommandHandler('insert', insert)],
        states={
             # Функция считывает номер записи, которую мы хотим ДРОПНУТЬ
            1: [MessageHandler(Filters.text & ~Filters.command, execute_insert)] },
        fallbacks=[CommandHandler('stop', stop)]
                                    )
    #---- ПОИСК записей по ИМЕНИ --------------
find_records = ConversationHandler(
        entry_points=[CommandHandler('find', find)],
        states={
             # Функция КУСОК имени для поиска
            1: [MessageHandler(Filters.text & ~Filters.command, execute_find)] },
        fallbacks=[CommandHandler('stop', stop)]
                                    )


start_handler = CommandHandler('start', start)
open_handler = CommandHandler('open', open)



dispatcher.add_handler(start_handler)
dispatcher.add_handler(open_handler)
# dispatcher.add_handler(insert_handler)
dispatcher.add_handler(new_records)
dispatcher.add_handler(find_records)

dispatcher.add_handler(delete_records)
dispatcher.add_handler(edit_records)






# ----- запускает цикл приема и обработки сообщений ----
updater.start_polling()
# ----- ждет завершения приложения -----
updater.idle()