from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import  datetime

import spy_data
from spy_data import *


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy_data.log_command(update, context)
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy_data.log_command(update, context)
    await update.message.reply_text(f'/hi - приветствие \n/time - текущее время\n/sum -сумма 2 + 3  \n')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    spy_data.log_command(update, context)
    await update.message.reply_text(f'Время {datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = update.message.text
    chislo1 = int(msg.split()[1])
    chislo2 = int(msg.split()[2])
    spy_data.log_command(update, context)
    await update.message.reply_text(f'{chislo1} + {chislo2} = {chislo1 + chislo2}')

