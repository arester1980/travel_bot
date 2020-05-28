import telebot
import config
from geopy import Nominatim, distance
from random import uniform

MYPLACE = (53.902221, 27.561924)

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def get_locate(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    button_get = telebot.types.InlineKeyboardButton(text='Get location')
    keyboard.add(button_get)
    bot.send_message(message.chat.id, 'Press button', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def coordi(message):
    if message.text == 'Get location':
        x = round(uniform(51.262, 56.172), 4)
        y = round(uniform(23.178, 32.777), 4)
        x, y = str(x), str(y)
        coord = '{},{}'.format(x, y)
        geolocator = Nominatim(user_agent='geobot')
        location = geolocator.reverse(coord)
        r = location.raw
        adr = r.get('address')
        cc = adr.get('country_code')
        loc = location.address
        dist = distance.distance(MYPLACE, coord)
        dist = str(dist)
        dist = 'Distance from Minsk to this place: {} km'.format(dist[0:3:])
        link = 'https://www.google.com/maps/place/{}'.format(coord)
        if cc == 'by':
            bot.send_message(message.chat.id, loc)
            bot.send_message(message.chat.id, link)
            bot.send_message(message.chat.id, dist)
        else:
            print('None BY')
            coordi(message)


bot.polling()
