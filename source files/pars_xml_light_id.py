from xml.dom import minidom
import random

doc = minidom.parse('priluki.xml')
points=doc.getElementsByTagName('node')

list_id = []

for p in points:
	list_id.append(p.getAttribute('id'))

rndm_id = random.choice(list_id)
print('Случайный node для региона Прилуки: ', end='')
print('https://www.openstreetmap.org/node/{}'.format(rndm_id))