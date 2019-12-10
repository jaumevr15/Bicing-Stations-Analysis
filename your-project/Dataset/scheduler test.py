
# import libraries
import pybikes
import time
import datetime
import pandas as pd
import requests

bicing = pybikes.get('bicing')

# Define variables
stations = []
## define current time + 24 hours
endtime=time.time() + 597600.0   #86400 for 24 hours 604800 for a week
## define the name of the  csv file where the result of the bicing stations will be saved
today = str(datetime.date.today())
file_name = "bicing" + today + ".csv"
## Define the url name of the Bicing website
url = 'https://www.bicing.barcelona/get-stations'


# Define functions
## Define a function to get the bikes in the bicing stations until time_s
def result(time_s):
    while (time.time()<time_s):
        now = datetime.datetime.now()
        print(str(now))
        try:
            bicing.update()
            print(requests.get(url).status_code)
            for station in bicing.stations:
                lat = station.latitude
                lon = station.longitude
                uid = station.extra['uid']
                bikes = station.bikes
                free_slots = station.free
                stations.append([now, uid, bikes, free_slots, lat, lon])
            time.sleep(900)
        except ValueError:
            time.sleep(900)
            continue
    return stations

# Define a function to save the stations list in a csv with the date included in the file name.
def transfer_csv(lst, file_n):
    df = pd.DataFrame(lst)
    file = df.to_csv(file_n)
    return file

result(endtime)
transfer_csv(stations, file_name)

