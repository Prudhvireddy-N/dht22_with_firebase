#!/usr/bin/python

import sys
import time
import Adafruit_DHT

while True:
    humidity, temperature = Adafruit_DHT.read_retry(22, 22)
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    time.sleep(2)


