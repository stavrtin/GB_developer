from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bots_commands


app = ApplicationBuilder().token("5457794399:AAHZVbSVwyH8fmtjzkWojUyt5786Nipb6h8").build()

app.add_handler(CommandHandler("hi", bots_commands.hi_command))
app.add_handler(CommandHandler("time", bots_commands.time_command))
app.add_handler(CommandHandler("help", bots_commands.help_command))
app.add_handler(CommandHandler("sum", bots_commands.sum_command))

print('Bot STARTs')

app.run_polling()
