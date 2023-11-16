from flask import Flask, request

from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater, ApplicationBuilder, ContextTypes
import configparser

app = Flask(__name__)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
# bot = Bot(token='6589718266:AAHKFM9wwTTPCFCcwtiblLATHccCPLMHU1w')
config = configparser.ConfigParser()
config.read('config.ini')
application = ApplicationBuilder().token(config['TELEGRAM']['ACCESS_TOKEN']).build()

# updater = Updater(bot=bot, update_queue=Que)
# dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your simple Flask-based Telegram bot.')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update)
    print(context)
    print(context.args)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

# Register the command handler
app.add_url_rule('/start', 'start', lambda: '', methods=['POST'])
application.add_handler(CommandHandler('start', start))



@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.process_update(update)
    return 'OK'


if __name__ == '__main__':
    # Set your webhook URL, e.g., https://your-domain.com/webhook
    webhook_url = 'https://api.telegram.org/bot6589718266:AAHKFM9wwTTPCFCcwtiblLATHccCPLMHU1w/setWebhook?url=https://api.render.com/deploy/srv-cl8du7f6e7vc73a54efg?key=2Zq6rsuV8zQ'

    # Set your webhook secret token
    # secret_token = '6589718266:AAHKFM9wwTTPCFCcwtiblLATHccCPLMHU1w'

    # Start the Flask app with webhook configuration
    app.run(port=5000, debug=True)
