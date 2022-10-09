from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
# import bots_commands

def log_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_log = open('db.csv', 'a')
    file_log.write(f'{datetime.datetime.now().time()}, {update.effective_user.first_name}, {update.effective_user.id}, {update.effective_user.last_name}, {update.chat_member}\n')
    file_log.close()
