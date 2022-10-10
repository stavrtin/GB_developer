from telegram import Bot
import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from tok import token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)



def start(update, content):
    content.bot.send_message(update.effective_chat.id, "Привет. Я - бот-калькулятор!"
                                                       "я могу считать по команде /calc "
                                                       "я могу конвертировать по команде /convert")


def info(update, content):
    content.bot.send_message(update.effective_chat.id, "Это - бот!")


def echo(update, context):
    update.message.reply_text(update.message.text)


def calc(update, content):
    content.bot.send_message(update.effective_chat.id, "Введите выражение для вычисления"
                                                       "что бы выйти - нажмите /stop")
    return 1


def convert(update, content):
    content.bot.send_message(update.effective_chat.id, "Введите длину в километрах"
                                                       "что бы выйти - нажмите /stop")
    return 1


def eval_calculate(update, content):
    try:
        content.bot.send_message(update.effective_chat.id, f'Результат {update.message.text} = {eval(update.message.text)}')
    except Exception:
        content.bot.send_message(update.effective_chat.id,
                                 f'Ну криво вводишь - смотри, что печатаешь!')
        logging.warning("Некоректное выражение")

    # return ConversationHandler.END

def eval_convert(update, content):
    lenth = int(update.message.text)
    lenth_convert = lenth * 1000
    content.bot.send_message(update.effective_chat.id, f'Расстояние в {lenth} км = {lenth_convert} метрам')
    # return ConversationHandler.END

def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


bot_token = token
bot = Bot(bot_token)
updater = Updater(bot_token,  use_context=True)
dispatcher = updater.dispatcher

calc_handler = ConversationHandler(
        entry_points=[CommandHandler('calc', calc)],
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(Filters.text & ~Filters.command, eval_calculate)],
        }
    ,
        fallbacks=[CommandHandler('stop', stop)]
    )


conv_handler = ConversationHandler(
        entry_points=[CommandHandler('convert', convert)],
        states={
            # Функция читает ответ на первый вопрос и задаёт второй.
            1: [MessageHandler(Filters.text & ~Filters.command, eval_convert)],

        },
        fallbacks=[CommandHandler('stop', stop)]
    )


start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)



dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(calc_handler)
dispatcher.add_handler(conv_handler)



# ----- запускает цикл приема и обработки сообщений ----
updater.start_polling()
# ----- ждет завершения приложения -----
updater.idle()