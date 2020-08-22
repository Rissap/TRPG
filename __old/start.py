import settings
import src.world as world

import os
import time
import random
import signal


from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
#from telegram.ext.dispatcher import run_async


UPDATER = Updater(token=settings.TOKEN, use_context=True)
DISPATCHER = UPDATER.dispatcher
PROCESS = world.ProcessRequest()


def stop(update, context):
    PROCESS.stop()
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я умру, Лисы останутся.")
    os.kill(os.getpid(), signal.SIGINT)


#@run_async
def echo(update, context):
    user = update.message.from_user["id"]
    message = update.message.text

    reply, keyboard = PROCESS.process(user, message)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=reply,
        reply_markup=keyboard
    )


start_handler = CommandHandler('start', echo)
stop_handler = CommandHandler('stop', stop)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

DISPATCHER.add_handler(echo_handler)
DISPATCHER.add_handler(start_handler)
DISPATCHER.add_handler(stop_handler)

UPDATER.start_polling()

