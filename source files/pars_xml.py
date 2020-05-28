from xml.dom import minidom


doc = minidom.parse('sea.xml')
points=doc.getElementsByTagName('node')

for p in points:
	print(p.getAttribute('id'))