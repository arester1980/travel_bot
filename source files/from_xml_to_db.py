from tinydb import TinyDB
from xml.dom import minidom

db = TinyDB('map_db/by.json')

def recDB(file):
	name = file.split('/')
	name = str(name[1])
	name = name.split('.')
	name = name[0]
	if name in db.tables():
		print('Table already exist!')
	else:
		create_table = db.table(name)
		table_ins = file[:-4]+'_table'
		print('Table created!')
		table = create_table
		doc = minidom.parse(file)
		points=doc.getElementsByTagName('node')
		list_id = []
		for p in points:
			k = 'node'
			list_id.append({k:p.getAttribute("id")})
		table.insert_multiple(list_id)
		
recDB('map_db/stolin.xml')