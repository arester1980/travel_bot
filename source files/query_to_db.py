from tinydb import TinyDB
from random import randint, choice


AREA = ['priluki', 'loev', 'stolin']

rndm_area = choice(AREA)

def get_node(file, table):
	global rndm_area 
	db = TinyDB(file)
	tab = db.table(table)
	range_list = len(tab)
	rndm_node = randint(0, range_list)
	tab = list(tab)
	res = str(tab[rndm_node])
	res = res.split("'")
	res = res[-2]
	rndm_area = rndm_area.title()
	return print('''Node is located in {} area.
Link to map: https://www.openstreetmap.org/node/{}'''.format(rndm_area, res))

get_node('by.json', rndm_area)