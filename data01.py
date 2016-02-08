import urllib.request
from xml.etree.ElementTree import parse
from operator import attrgetter
url = 'http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22'
''''req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
   data = response.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close'''
positions = []
class Position:
	def __init__(self, id, d, lat, lon,d_lat, d_lon, rank = None):
		self.id = id
		self.d = d
		self.lat = lat
		self.lon = lon
		self.d_lat = d_lat
		self.d_lon = d_lon
		self.rank = rank 
	def __repr__(self):
		return repr((self.id, self.lat, self.lon))

daves_latitude = 41.98062
daves_longitude = -87.668452
doc = parse('rt22.xml')
time = doc.findtext('time')
for bus in doc.findall('bus') :
	id = bus.findtext('id')	
	d = bus.findtext('d')
	lat = float(bus.findtext('lat'))
	lon = float(bus.findtext('lon'))
	d_lat = max((lat - daves_latitude),-1*(lat - daves_latitude))
	d_lon = max((lon - daves_longitude), -1*(lon - daves_longitude))
	rank = d_lat + d_lon
	print(id, time, d, lat, lon, d_lat, d_lon, str(rank))
	positions.append(Position(id, d, lat, lon, d_lat, d_lon, rank))
#ranks = sorted(positions, key=lambda position: position.rank)
ranks = sorted(positions, key = attrgetter('rank'))
for position in ranks:
	print (position.rank, position.id, position.lat, position.lon)
print ('----------------')

