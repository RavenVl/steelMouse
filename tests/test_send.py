import json

import pytest
import unittest
from unittest.mock import patch, mock_open
from unittest import mock
from send_time import SendTimeToMouse
import builtins


def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://127.0.0.1:59885/game_event':
        data = json.loads(kwargs['data'])
        data_etalon = {
            "game": "TEST_TIME",
            "event": "TICK",
            "data": {
                "value": "test"
            }
        }
        if data == data_etalon:
            return MockResponse({}, 200)
        else:
            return MockResponse({}, 400)
    elif args[0] == 'http://someotherurl.com/anothertest.json':
        return MockResponse({}, 200)

    return MockResponse({}, 404)


class TestSendTime(unittest.TestCase):

    def test_init(self):
        simpleconfig = '{"address":"127.0.0.1:59885","encrypted_address":"127.0.0.1:59886"}'
        open_ = mock_open(read_data=simpleconfig)
        with patch.object(builtins, "open", open_):
            sender = SendTimeToMouse()
            self.assertEqual("http://127.0.0.1:59885", sender.base_addr)

    @mock.patch('send_time.requests.post', side_effect=mocked_requests_post)
    def test_send_event(self, mock_get):
        simpleconfig = '{"address":"127.0.0.1:59885","encrypted_address":"127.0.0.1:59886"}'
        open_ = mock_open(read_data=simpleconfig)
        with patch.object(builtins, "open", open_):
            sender = SendTimeToMouse()
            # send true data
            try:
                sender.send_event_tick('test')
            except ConnectionError:
                self.fail('ConnectionError exception raised')
            except Exception:
                self.fail('unexpected exception raised')
            # send false data
            with self.assertRaises(ConnectionError):
                sender.send_event_tick('test1')


if __name__ == '__main__':
    unittest.main()
