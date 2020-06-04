from geopy import Nominatim, distance
from random import uniform
import telebot
import jsonpickle
# import os

# token = os.getenv("token")
bot = telebot.TeleBot('1171904194:AAGtjGvd_oKWFUOUa_DNg0o3UdrN7zR_sZk')

MINSK = (53.902221, 27.561924)
PRILUKI = (53.797048, 27.450923)

place = []
links = []

# 1171904194:AAGtjGvd_oKWFUOUa_DNg0o3UdrN7zR_sZk


@bot.message_handler(commands=['start'])
def get_locate(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    button_get = telebot.types.InlineKeyboardButton(text='Любая точка Беларуси')
    button_bike = telebot.types.InlineKeyboardButton(text='Точка на определенном расстоянии от тебя')
    keyboard.add(button_get)
    keyboard.add(button_bike)
    bot.send_message(message.chat.id, 'Выбери какую точку хотел бы получить', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_data(message):
    if message.text == 'Любая точка Беларуси':
        lon = round(uniform(51.262, 56.172), 4)
        lat = round(uniform(23.178, 32.777), 4)
        lon, lat = str(lon), str(lat)
        coord = '{},{}'.format(lon, lat)
        geolocator = Nominatim(user_agent='geobot')
        location = geolocator.reverse(coord) # получаем место на карте по координатам
        r = location.raw # получаем json
        adr = r.get('address')  # из json берем адрес
        cc = adr.get('country_code') # из адреса берем код страны
        if cc == 'by':
            place.clear()
            loc = location.address  # строка с человекочитаемым адресом
            place.append(coord) # переписываем значение координат места
            place.append(loc)
            dist = distance.distance(MINSK, coord)  # вычисление расстояния между Минском и адресом
            dist = str(dist)
            dist = dist.split(' ')
            dist = round(float(dist[0]), 2)  # округленное значение расстояния
            dist = 'Растояние от Октябрьской площади Минска до этого места: {} km.\nЧто бы узнать расстояние от ' \
                    'твоего местонахождения до {} пришли боту свою геолокацию или проложи свой маршрут с ' \
                    'использованием одного из сервисов'.format(dist, loc.split(',')[0])
            links.clear()
            links.append('Это место на картах Google":\nhttps://www.google.com/maps/place/{}'.format(coord))
            links.append('Это место на картах Yandex:\nhttps://yandex.com/maps/?text={}'.format(coord))
            links.append('Это место на картах архитектурного наследия Беларуси:\nhttps://orda.of.by/.map/?{}'.format(coord))
            links.append('Это место на картах MapsMe:\nmaps.google.com/{}'.format(coord))
            keyboard = telebot.types.InlineKeyboardMarkup()
            key_ya = telebot.types.InlineKeyboardButton(text='Yandex', callback_data='ya')
            key_gg = telebot.types.InlineKeyboardButton(text='Google', callback_data='gg')
            key_globus = telebot.types.InlineKeyboardButton(text='карты Globus.tut.by', callback_data='globus')
            key_maps = telebot.types.InlineKeyboardButton(text='приложение Maps.me', callback_data='maps')
            keyboard.add(key_ya, key_gg)
            keyboard.add(key_globus, key_maps)
            bot.send_message(message.chat.id, "Почему бы сегодня не отправится:\n{}".format(loc))
            bot.send_message(message.chat.id, dist, reply_markup=keyboard)
        else:
            print('None BY')
            get_data(message)
    if message.text == 'Точка на определенном расстоянии от тебя':
        bot.send_message(message.chat.id, 'Введите количество километров, которое ты готов преодолеть. Точка будет на этом расстоянии +/- 20%')
    else:
        parc(message)

def parc(message):
    # message = message.text
    # print(message)
    x_json = jsonpickle.encode(message)
    x_list = x_json.split(':')
    x_rawtext = x_list[82]
    x_text = x_rawtext.replace('"', '')
    x_text = x_text.rstrip('}')
    x_text = x_text.replace(' ', '') # содержание сообщения
    print(x_text)
    if x_text.isnumeric(): # проверка сообщения на число
        rang = int(x_text)
        coord, rang_rng = loc_coord(rang) # вернулся диапазон расстояний 20%
        geolocator = Nominatim(user_agent='geobot')
        location = geolocator.reverse(coord) # получаем место на карте по координатам
        dist = distance.distance(PRILUKI, coord)
        dist = str(dist)
        dist = dist.split(' ')
        dist = round(float(dist[0])) # из введенного пользователя значения получаем километраж
        if dist in rang_rng:
            adr = location.address
            place.append(adr)
            dist = str(dist)
            dist = dist.split(' ')
            dist = round(float(dist[0]), 2)  # округленное значение расстояния
            dist = 'Растояние от Прилук до {} этого места: {} km'.format(adr, dist)
            bot.send_message(message.chat.id, dist)
        else:
            print('another distance')
            parc(message)
    else:
        bot.send_message(message.chat.id, 'Введите число')

def loc_coord(rang):
    global coord
    rang_prc = rang/5 #20 процентов от желаемой дистанции
    rang_min = int(rang-rang_prc)
    rang_max = int(rang+rang_prc)
    rang_rng = [i for i in range(rang_min, rang_max)] # список расстояний от минимального до макисмального
    if rang >= 350:
        lon = round(uniform(54.551550, 56.172), 4)
        lat = round(uniform(30.224864, 32.777), 4)
        lon, lat = str(lon), str(lat)
        lon, lat = str(lon), str(lat)
        coord = '{},{}'.format(lon, lat)
    if rang < 350 > 250:
        lon = round(uniform(54.551549, 55.198531), 4)
        lat = round(uniform(29.240142, 30.224863), 4)
        lon, lat = str(lon), str(lat)
        coord = '{},{}'.format(lon, lat)
    if rang < 250 > 100:
        lon = round(uniform(54.318075, 54.551548), 4)
        lat = round(uniform(28.721071, 29.240141), 4)
        lon, lat = str(lon), str(lat)
        coord = '{},{}'.format(lon, lat)
    if rang < 100:
        lon = round(uniform(53.527442, 54.318074), 4)
        lat = round(uniform(26.388708, 28.721070), 4)
        lon, lat = str(lon), str(lat)
        coord = '{},{}'.format(lon, lat)
    return coord, rang_rng

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global links
    if call.data == "ya":
        bot.send_message(call.message.chat.id, links[1])
    if call.data == "gg":
        bot.send_message(call.message.chat.id, links[0])
    if call.data == "globus":
        bot.send_message(call.message.chat.id, links[2])
    if call.data == "maps":
        bot.send_message(call.message.chat.id, links[3])


@bot.message_handler(content_types=['location'])
def calc_distance(message):
    global place
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
    y = place[0].split(',')
    place_float = []
    # place_float.clear()
    for i in y:
        place_float.append(float(i))
    yourdist = str(distance.distance(loc_float, place_float))
    yourdist = yourdist.split(' ')
    yourdist = round(float(yourdist[0]), 2)
    your_place = place[1]
    bot.send_message(message.chat.id, 'Расстояние от тебя до {}: {} km'.format(your_place.split(',')[0], yourdist))


bot.polling()