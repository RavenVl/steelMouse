from os import path
import json
import requests
import time

def send_req(data, adr):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    resp = requests.post(adr, data=json.dumps(data), headers=headers)
    print(resp.status_code, resp.json())

path_ini = path.join("c:\ProgramData\SteelSeries\SteelSeries Engine 3\coreProps.json")
with open(path_ini) as file:
    temp = json.load(file)

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


send_req(meta_time, address_meta)

game_event = {
  "game": "TEST_TIME",
  "event": "TICK",
  "icon_id": 1,
  "handlers": [
      {
          "device-type": "screened",
          "mode": "screen",
          "zone": "one",
          "datas": [{
              "has-text": True,
              "context-frame-key": "custom-text"
          }]
      }
  ]
}

addr_bind_events = 'http://' + temp['address'] + '/bind_game_event'
send_req(game_event, addr_bind_events)

event_context = {
  "game": "TEST_TIME",
  "event": "TICK",
  "data": {
      "value": 75,
      "frame": {
        "custom-text": "Temp text value"
      }
  }
}

address_events = 'http://' + temp['address'] + '/game_event'
send_req(event_context, address_events)

