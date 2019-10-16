#!/usr/local/bin/python3

import json
import requests

class Input:
    def __init__(self, method = 'api'):
        if method not in ['api', 'file']:
            raise ValueError('method is only allowed to be api or file')
        self.method = method

    def get(self):
        if self.method == 'api':
            return self.api_input()
        return self.file_input()

    def _parse_line(self, line):
        parsed_line = {}
        try:
            parsed_line = json.loads(line)
        except:
            pass
        return parsed_line

    def file_input(self, filename='meetup.json', termination_limits = 1000):
        processed_lines = 0
        with open(filename) as f:
            for line in f:
                processed_lines += 1
                if processed_lines > termination_limits:
                    return iter([])
                yield self._parse_line(line)

    def api_input(self, api='http://stream.meetup.com/2/rsvps', termination_limits = 10000):
        processed_lines = 0
        with requests.get(url = api, stream = True) as resp:
            for line in resp.iter_lines():
                processed_lines += 1
                if processed_lines > termination_limits:
                    return iter([])
                yield self._parse_line(line)
