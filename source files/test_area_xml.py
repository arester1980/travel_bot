from xml.dom import minidom
from random import choice, randint
import random


AREA = {1: ['Лоевском', 'loev.xml'], 2: ['Столинском', 'stolin.xml']}

rndm_area = randint(1,2) # генерация числа для определения района
curr_area = AREA.get(rndm_area) # получаем значение из словаря
foo_area = curr_area[1] # получаем название файла для функции

print(f'Локация в {curr_area[0]} районе')

def coord(file):
	doc = minidom.parse(file)
	points=doc.getElementsByTagName('node')
	list_id = []
	for p in points:
		list_id.append(p.getAttribute('id'))
	x = random.choice(list_id)
	print('https://www.openstreetmap.org/node/{}'.format(x))

coord(foo_area)