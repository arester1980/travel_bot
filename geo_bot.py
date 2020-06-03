from geopy import Nominatim, distance
from random import uniform
import telebot
import jsonpickle
# import os
#
# token = os.getenv("token")
bot = telebot.TeleBot('1171904194:AAGtjGvd_oKWFUOUa_DNg0o3UdrN7zR_sZk')


# MINSK = (53.902221, 27.561924)

place = []
links = []

# 1171904194:AAGtjGvd_oKWFUOUa_DNg0o3UdrN7zR_sZk


@bot.message_handler(commands=['start'])
def get_locate(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    # button_get = telebot.types.InlineKeyboardButton(text='Куда отправиться?')
    # button_bike = telebot.types.InlineKeyboardButton(text='Точка в радиусе')
    # keyboard.add(button_get)
    # keyboard.add(button_bike)
    # bot.send_message(message.chat.id, 'Сколько километров хочешь проехать?', reply_markup=keyboard)
    bot.send_message(message.chat.id, 'Сколько километров хочешь проехать?')


@bot.message_handler(content_types=['text'])
def get_data(message):
    x_json = jsonpickle.encode(message)
    x_list = x_json.split(':')
    x_rawtext = x_list[82]
    x_text = x_rawtext.replace('"', '')
    x_text = x_text.rstrip('}')
    x_text = x_text.replace(' ', '')
    if x_text.isnumeric():
        rang = int(x_text)
        km = 10+rang
        bot.send_message(message.chat.id, km)
    else:
        bot.send_message(message.chat.id, 'Введите число')

# def coordi(message):
#     if message.text == 'Куда отправиться?': # случайные координаты в приблизительных границах Беларуси
#         lon = round(uniform(51.262, 56.172), 4)
#         lat = round(uniform(23.178, 32.777), 4)
#         lon, lat = str(lon), str(lat)
#         coord = '{},{}'.format(lon, lat)
#         geolocator = Nominatim(user_agent='geobot')
#         location = geolocator.reverse(coord) # получаем место на карте по координатам
#         r = location.raw # получаем json
#         adr = r.get('address')  # из json берем адрес
#         cc = adr.get('country_code') # из адреса берем код страны
#         if cc == 'by':
#             place.clear()
#             loc = location.address  # строка с человекочитаемым адресом
#             place.append(coord) # переписываем значение координат места
#             place.append(loc)
#             dist = distance.distance(MINSK, coord)  # вычисление расстояния между Минском и адресом
#             dist = str(dist)
#             dist = dist.split(' ')
#             dist = round(float(dist[0]), 2)  # округленное значение расстояния
#             dist = 'Растояние от Октябрьской площади Минска до этого места: {} km.\nЧто бы узнать расстояние от ' \
#                    'твоего местонахождения до {} пришли боту свою геолокацию или проложи свой маршрут с ' \
#                    'использованием одного из сервисов'.format(dist, loc.split(',')[0])
#             links.clear()
#             links.append('Это место на картах Google":\nhttps://www.google.com/maps/place/{}'.format(coord))
#             links.append('Это место на картах Yandex:\nhttps://yandex.com/maps/?text={}'.format(coord))
#             links.append('Это место на картах архитектурного наследия Беларуси:\nhttps://orda.of.by/.map/?{}'.format(coord))
#             links.append('Это место на картах MapsMe:\nmaps.google.com/{}'.format(coord))
#             keyboard = telebot.types.InlineKeyboardMarkup()
#             key_ya = telebot.types.InlineKeyboardButton(text='Yandex', callback_data='ya')
#             key_gg = telebot.types.InlineKeyboardButton(text='Google', callback_data='gg')
#             key_globus = telebot.types.InlineKeyboardButton(text='карты Globus.tut.by', callback_data='globus')
#             key_maps = telebot.types.InlineKeyboardButton(text='приложение Maps.me', callback_data='maps')
#             keyboard.add(key_ya, key_gg)
#             keyboard.add(key_globus, key_maps)
#             bot.send_message(message.chat.id, "Почему бы сегодня не отправится:\n{}".format(loc))
#             bot.send_message(message.chat.id, dist, reply_markup=keyboard)
#         if message == 'Точка в радиусе':
#             send = bot.message_handler(commands=['text'])
#             bot.register_next_step_handler(send, get_data)
#             # bike.append(send)
#         else:
#             print('None BY')
#             coordi(message)


# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     global links
#     if call.data == "ya":
#         bot.send_message(call.message.chat.id, links[1])
#     if call.data == "gg":
#         bot.send_message(call.message.chat.id, links[0])
#     if call.data == "globus":
#         bot.send_message(call.message.chat.id, links[2])
#     if call.data == "maps":
#         bot.send_message(call.message.chat.id, links[3])


# @bot.message_handler(content_types=['location'])
# def calc_distance(message):
#     global place
#     x = jsonpickle.encode(message)
#     xs = x.split(',')
#     xsr = xs[78:80]
#     lat = []
#     lon = []
#     for i in xsr[0]:
#         if i.isdigit() or i == '.':
#             lat.append(i)
#     for i in xsr[1]:
#         if i.isdigit() or i == '.':
#             lon.append(i)
#     loc_list = [''.join(lat), ''.join(lon)]
#     loc_float = []
#     for i in loc_list:
#         loc_float.append(float(i))
#     y = place[0].split(',')
#     place_float = []
#     # place_float.clear()
#     for i in y:
#         place_float.append(float(i))
#     yourdist = str(distance.distance(loc_float, place_float))
#     yourdist = yourdist.split(' ')
#     yourdist = round(float(yourdist[0]), 2)
#     your_place = place[1]
#     bot.send_message(message.chat.id, 'Расстояние от тебя до {}: {} km'.format(your_place.split(',')[0], yourdist))


bot.polling()