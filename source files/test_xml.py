import xml.dom.minidom
import random


# lat = [randint(0,90) for x in range(2)]
# lon = [randint(-180,180) for x in range(2)]
lat = round(random.uniform(0, 90), 6)
lon = round(random.uniform(-180, 180), 6)

print('https://www.openstreetmap.org/export#map=14/{}/{}'.format(lat, lon))
# print(link)

doc = xml.dom.minidom.parse('map.osm')
x = doc.getElementsByTagName('tag')
for val in x:
	print(val)
# if x is False:
# 	print('Yes')
# else:
# 	print('No')
# for k in x:
 	# print(k)


# # tag k="name:ru"

# https://overpass-api.de/api/map?bbox={},{},{},{}