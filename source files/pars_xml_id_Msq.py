import random

c = True

while c == True:
	f=open('minsk.xml', encoding='utf8')
	i=0
	for line in f:
		i
		i+=1
	rndm_str = random.randint(1, i)
	f=open('minsk.xml', encoding='utf8')
	i=0
	for line in f:
		i
		i+=1
		if i == rndm_str:
			if 'id=' in line:
				node_id = line.split(' ')
				clear_id = node_id[3]
				x = clear_id[4:-1]
				print('Случайный node для города Минск: ', end='')
				print('https://www.openstreetmap.org/node/{}'.format(x))
				c = False
			else:
				print('{} здесь node нет. Продолжаем искать... '.format(line))
				c = True
print(c)