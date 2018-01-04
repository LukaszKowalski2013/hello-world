
import csv
from time import gmtime, strftime
import time
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

myOutputMatrix = open(r"F:\pythonGames\PythonGames\darkSkyAPI\data\myMatrix.csv", "w") #output

# https://api.darksky.net/forecast/[key]/[latitude],[longitude]

myKey = 'e97bae9d06a69efc156e0a7da0a5a904'

call = 'https://api.darksky.net/forecast/e97bae9d06a69efc156e0a7da0a5a904/51.512841,-0.114895'

# 25 - 31 X
s="" #here we write down our data

for day in range (24, 31):

    date_time = str(day) + '.10.2017 23:00:00'
    pattern = '%d.%m.%Y %H:%M:%S'
    epoch = int(time.mktime(time.strptime(date_time, pattern)))
    print(epoch)

    url = call + "," + str(epoch)
    ctx = ssl.create_default_context()
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    js = json.loads(data)

    for i in range(0, 24):
    #data
        mytime = js['hourly']['data'][i]['time']
        mon = time.gmtime(mytime).tm_mon
        day = time.gmtime(mytime).tm_mday
        hour = time.gmtime(mytime).tm_hour

        s+= str(js['hourly']['data'][i]['time'])+ ", " + str(js['hourly']['data'][i]['apparentTemperature'])+", "+ str(js['hourly']['data'][i]['precipType'])+", " + str(js['hourly']['data'][i]['icon'])+ "," + str(js['hourly']['data'][i]['humidity'])+", "+ str(js['hourly']['data'][i]['windSpeed']) + "\n"

stringToWrite = s
myOutputMatrix.write(stringToWrite)
myOutputMatrix.close()