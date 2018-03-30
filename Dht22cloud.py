#!/usr/bin/python

import sys
import time
import Adafruit_DHT
import json
from firebase import firebase

#firebase_url= "https://tank-1fbad.firebaseio.com"
firebase = firebase.FirebaseApplication('https://tank-1fbad.firebaseio.com/')

while True:
    humidity, temperature = Adafruit_DHT.read_retry(22, 22)
    print('temperature={0:0.1f}*  humidity={1:0.1f}%'.format(temperature, humidity))
    
    #data={'value':temperature,'value':humidity }
    result = firebase.post('/DHT22',{'temperature:temperature','humidity:humidity'})
    #result = firebase.post(firebase_url + '/' + '/temperature.json' +'/humidity.json',data=json.dumps(data))
    print (result)
    time.sleep(2)  


