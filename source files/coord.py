import random

nosoli=['N', 'S']
nososel=random.choice(nosoli)
eaweli=['E', 'W']
eawesel=random.choice(eaweli)
width=random.uniform(0,90)
widthcorr=round(width,2)
heigh=random.uniform(0,180)
heighcorr=round(heigh,2)
coord='{}{}, {}{}'.format(nososel, widthcorr, eawesel, heighcorr)
print(coord)