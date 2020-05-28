import random
import telebot
import config


bot = telebot.TeleBot(config.token)
keyboard = telebot.types.ReplyKeyboardMarkup(True)
button_get = telebot.types.InlineKeyboardButton('Get random location')
keyboard.add(button_get)


@bot.message_handler(commands=['start'])
def get_locate(message):
    bot.send_message(message.chat.id, 'Press button', reply_markup=keyboard)


@bot.message_handler(commands=['getlocation'])
def get_locate(message):
    width = round(random.uniform(-90, 90), 6)
    heigh = round(random.uniform(-180, 180), 6)
    bot.send_location(message.chat.id, width, heigh)


@bot.message_handler(content_types=['text'])
def get_locate(message):
    if message.text == 'Get random location':
        width = round(random.uniform(-90, 90), 6)
        heigh = round(random.uniform(-180, 180), 6)
        bot.send_location(message.chat.id, width, heigh)


bot.polling()
