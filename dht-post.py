#import RPi.GPIO as GPIO
from time import sleep
import datetime
import Adafruit_DHT
import urllib2, urllib, httplib
import json
import os
import requests
import sys

sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    sys.exit(1)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)


def update_post():

	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
		sleep(5)
		str_temp = ' {0:0.2f} *C '.format(temperature)	
		str_hum  = ' {0:0.2f} %'.format(humidity)
		print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))	
			
	else:
		print('Failed to get reading. Try again!')	
		sleep(10)

	data = {'devId':'Dev001',
                'temp':temperature,
                'co2':0.876,
                'co':0.756,
                'humidity':humidity,
                'lpg':0.009,
                'smoke':0.05,
                'doe':'2018-03-30T04:33:33.580Z'}        
        PostURL = 'https://andropi.azurewebsites.net/insertData'
        headers = {'content-type': 'application/json'}

        res = requests.post(url = PostURL, data = json.dumps(data), headers=headers)

        print(res.json()) 
	

while True:
		update_post()
		
        #sleepTime = int(sleepTime)
		sleep(5)
	








