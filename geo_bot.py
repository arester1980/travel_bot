import config
from geopy import Nominatim, distance
from random import uniform
import telebot
import jsonpickle

MINSK = (53.902221, 27.561924)
place = []

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
        dist = distance.distance(MINSK, coord)
        dist = str(dist)
        dist = dist.split(' ')
        dist = round(float(dist[0]), 2)
        dist = 'Distance between Minsk and this place: {} km.\nIf you want to know distance between you and this place ' \
               'send your location to bot'.format(dist)
        link_gg = 'https://www.google.com/maps/place/{}'.format(coord)
        link_ya = 'https://yandex.com/maps/?text={}'.format(coord)
        link_ord = 'https://orda.of.by/.map/?{}'.format(coord)
        link_maps = 'maps.google.com/{}'.format(coord)
        if cc == 'by':
            place.clear()
            place.append(coord)
            bot.send_message(message.chat.id, "Why don't you go to:\n{}".format(loc))
            bot.send_message(message.chat.id, link_gg)
            bot.send_message(message.chat.id, dist)
            bot.send_message(message.chat.id, 'This place on Yandex:\n{}'.format(link_ya))
            bot.send_message(message.chat.id, 'This place on Globus:\n{}'.format(link_ord))
            bot.send_message(message.chat.id, 'This place on MapsMe:\n{}'.format(link_maps))
        else:
            print('None BY')
            coordi(message)


@bot.message_handler(content_types=['location'])
def calc_distance(message):
    global place
    x = message
    x = jsonpickle.encode(message)
    xs = x.split(',')
    xsr = xs[78:80]
    lat = []
    lon = []
    for i in xsr[0]:
        if i.isdigit() or i == '.':
            lat.append(i)
    for i in xsr[1]:
        if i.isdigit() or i == '.':
            lon.append(i)
    loc_list = [''.join(lat), ''.join(lon)]
    loc_float = []
    for i in loc_list:
        loc_float.append(float(i))
    x = place[0].split(',')
    place_float = []
    for i in x:
        place_float.append(float(i))
    yourdist = distance.distance(loc_float, place_float)
    yourdist = str(yourdist)
    yourdist = yourdist.split(' ')
    yourdist = round(float(yourdist[0]), 2)
    res = 'Distance between your and this place: {} km'.format(yourdist)
    bot.send_message(message.chat.id, res)


bot.polling()
