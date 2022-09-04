import os
import telegram.ext

API_KEY = os.getenv('API_KEY')
API_KEY = "***************************************************"


def start(update, context):
    update.message.reply_text("Hello! Welcome To Our services")


def help(update, context):
    update.message.reply_text("""The following commands are available:
    
    /start -> Welcome Message
    /help -> This Message
    /content -> Information About NeuralNine Content
    """)


def content(update, context):
    update.message.reply_text("We have videos and books! Watch and read them!")


def contact(update, context):
    update.message.reply_text("you can contact florian to the Discord Server.")


def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}")
    if update.message.text == "mohit":
        print(type(update.message.text))
    else:
        print(update.message.text)


updater = telegram.ext.Updater(API_KEY, use_context=True)
disp = updater.dispatcher


disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("contact", contact))
disp.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.text, handle_message))


updater.start_polling()
updater.idle()
