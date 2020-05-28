from geopy.geocoders import Nominatim
from random import uniform



def coord():
    x = round(uniform(51.262, 56.172), 4)
    y = round(uniform(23.178, 32.777), 4)
    x, y = str(x), str(y)
    coord = '{},{}'.format(x, y)
    return coord

def res(coord):
    global coordi
    geolocator = Nominatim(user_agent='geobot')
    location = geolocator.reverse(coord)
    r = location.raw
    adr = r.get('address')
    cc = adr.get('country_code')
    if cc == 'by':
        print(location.address)
        print('https://www.google.com/maps/place/{}'.format(coord))
    else:
        print('None BY')
        coord()
        res(coordi)

coordi = coord()

coord()
res(coord())