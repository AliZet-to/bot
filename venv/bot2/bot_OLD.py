# import telebot
import config
import random
from telegram.ext import *
import requests
import re
import sys
import json
import pprint


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def stop(update, context):
    print('Good-bye')
    sys.exit()

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def showMyLoc(update, context):
    # context.bot.send_message(chat_id=update.effective_chat.id, text="My Location is ")
    # pprint.pprint(json.dumps(update.message))
    # print(update.message)
    print(update.message)



updater = Updater(token=config.TOKEN, use_context=True)
dispatcher = updater.dispatcher


# ----------- BOT Commands Creation ----------------
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handler)


echo_handler = MessageHandler(Filters.text, echo) ### Returns ANY input by user TEXT
dispatcher.add_handler(echo_handler)


location_handler = MessageHandler(Filters.location, echo_handler) ### Returns ANY input by user TEXT
dispatcher.add_handler(location_handler)

# ------------ END of Commands Creation Block --------------


if __name__ == '__main__':
    updater.start_polling()