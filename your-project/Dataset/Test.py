import pybikes
import pandas as pd
import time
import datetime
import requests

bicing = pybikes.get('bicing')
print(bicing.meta)

print(len(bicing.stations))
bicing.update()

url = 'https://www.bicing.barcelona/get-stations'
print(requests.get(url).status_code)
print(len(bicing.stations))
print(type(bicing.stations[0]))

today = str(datetime.date.today())
print(today)
file_name = "bicing" + today + ".csv"
print(file_name)

stations = []
bicing.update()
for station in bicing.stations:
    name = station.name
    lat = station.latitude
    lon = station.longitude
    uid = station.extra['uid']
    bikes = station.bikes
    free_slots = station.free
    stations.append([uid, name, bikes, free_slots, lat, lon, ])

print(stations)

bike_stations = pd.DataFrame(stations)
bike_stations.head()