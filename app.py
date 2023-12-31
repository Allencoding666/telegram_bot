import logging
import telegram
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext.filters import MessageFilter
import configparser
from flask import Flask, request

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)

application = ApplicationBuilder().token(config['TELEGRAM']['ACCESS_TOKEN']).build()
bot = application.bot

@app.route('/hook', methods=['POST'])
def webhook_handler():
    """Set route /hook with POST method will trigger this method."""
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        # Update dispatcher process that handler to process this message
        dispatcher.process_update(update)
    return 'ok'




logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    print(context)
    print(context.args)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    print(context)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=say_hello())


async def bom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="金大聲")


def say_hello():
    return "Hello"


class FilterBom(MessageFilter):
    def filter(self, message):
        return "金打瞎" in message.text


if __name__ == '__main__':
    # start_handler = CommandHandler('start', start)
    # application.add_handler(start_handler)
    #
    # filter_bom = FilterBom()
    # filter_bom_handler = MessageHandler(filter_bom, bom)
    # application.add_handler(filter_bom_handler)
    #
    # echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    # application.add_handler(echo_handler)
    #
    #
    #
    # application.run_polling()
    app.run(debug=True)
