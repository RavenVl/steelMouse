import time
from os import path
import json
import requests


class SendTimeToMouse:
    path_ini = path.join("c:\ProgramData\SteelSeries\SteelSeries Engine 3\coreProps.json")

    def __init__(self):
        self.base_addr = self._get_addr_server()
        self._send_reg_app()
        self._send_reg_event()

    def _send_reg_app(self):
        address_meta = self.base_addr + '/game_metadata'
        meta_time = {
            "game": "TEST_TIME",
            "game_display_name": "My testing time",
            "developer": "Raven Studios"
        }
        self._send_req(meta_time, address_meta)

    def _send_reg_event(self):
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
                    }]
                }
            ]
        }

        addr_bind_events = self.base_addr + '/bind_game_event'
        self._send_req(game_event, addr_bind_events)

    def send_event_tick(self, text):
        event_context = {
            "game": "TEST_TIME",
            "event": "TICK",
            "data": {
                "value": text
            }
        }
        address_events = self.base_addr + '/game_event'
        self._send_req(event_context, address_events)

    def _send_req(self, data, adr):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        resp = requests.post(adr, data=json.dumps(data), headers=headers)

    def _get_addr_server(self):
        with open(self.path_ini) as file:
            addr = json.load(file)
        return 'http://' + addr['address']




if __name__ == '__main__':
    sender1 = SendTimeToMouse()
    for i in "some text":
        sender1.send_event_tick(i)
        time.sleep(1)

