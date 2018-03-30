import requests
import json

data = {'devId':'Dev001',
        'temp':111,
        'co2':0.876,
        'co':0.756,
        'humidity':0.987,
        'lpg':0.009,
        'smoke':0.05,
        'doe':'2018-03-30T04:33:33.580Z'}        
PostURL = 'https://andropi.azurewebsites.net/insertData'
headers = {'content-type': 'application/json'}

res = requests.post(url = PostURL, data = json.dumps(data), headers=headers)

print(res.json()) 