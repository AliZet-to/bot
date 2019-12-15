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
    pprint.pprint(json.dumps(update.message))



# bot = telebot.TeleBot(config.TOKEN)
updater = Updater(token=config.TOKEN, use_context=True)
dispatcher = updater.dispatcher

# --------------------- NEW CODE ----------------------------------------
# ----------- BOT Commands Creation ----------------
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handler)


echo_handler = MessageHandler(Filters.text, echo) ### Returns ANY input by user TEXT
dispatcher.add_handler(echo_handler)


location_handler = MessageHandler(Filters.location, showMyLoc) ### Returns ANY input by user TEXT
dispatcher.add_handler(location_handler)

# ------------ END of Commands Creation Block --------------



# @updater.message_handler(content_types=["location"])
# def location(bot, update):
#     message = None
#     if update.edited_message:
#         message = update.edited_message
#     else:
#         message = update.message
#     current_pos = (message.location.latitude, message.location.longitude)
#     print(current_pos)
#
# location_handler = MessageHandler(Filters.location, location)
# telegram.ext.Dispatcher.add_handler(location_handler)


if __name__ == '__main__':
    updater.start_polling()









# ------------ OLD CODE --------------
# emodji = ['😔', '😂', '☺', '️', '😁', '😒', '👍', '😘', '❤', '️', '😍', '😊', '😄', '😭', '💋', '😳', '😜', '🙈', '😉',
#           '😃']


# @bot.message_handler(commands=["hi"])
# def echo_all(message):
#     bot.send_message(message.chat.id, "Hello too")
#     inf = bot.get_me()
#     # print(inf.first_name)
#     bot.send_message(message.chat.id, "My name is " + inf.first_name)


# @bot.message_handler(content_types=["text"])
# def echo_all(message):
#     if message.text in emodji:
#         bot.send_message(message.chat.id, emodji[random.randint(0, 17)])
#     else:
#         bot.send_message(message.chat.id, message.text)

# @bot.message_handler(commands=["geo"])
# def geo(message):
#     keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_geo = telebot.types.KeyboardButton(text="Отправить местоположение", request_location=True)
#     keyboard.add(button_geo)
#     bot.send_message(message.chat.id, "Привет! Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)

# @bot.message_handler(content_types=["location"])
# def location(message):
#     if message.location is not None:
#         print(message.location)
#         print("latitude: %s; longitude: %s" % (message.location.latitude, message.location.longitude))

# ------------------ END of OLD CODE

