from os import path
import json
import requests
import time

path_ini = path.join("c:\ProgramData\SteelSeries\SteelSeries Engine 3\coreProps.json")
with open(path_ini) as file:
    temp = json.load(file)
address_events = 'http://' + temp['address'] + '/game_event'
address_meta = 'http://' + temp['address'] + '/game_metadata'

cur_time = time.time()
send_events = {
    "game": "CURENT TIME",
    "event": "TIME",
    "data": {
        "value": 75,
        "frame": {
            "<arbitrary key>": "value"
        }
    }
}

meta_time = {
    "game": "TEST_TIME",
    "game_display_name": "My testing time",
    "developer": "Raven Studios"
}

# r = requests.post(address_meta, json={'json_payload': meta_time})

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(address_meta, data=json.dumps(meta_time), headers=headers)
print(r.status_code, r.json())

