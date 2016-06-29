import urllib
import json

class Khepri:
    def __init__(self, url, api_key, instance_id):
        self.url = url
        self.api_key = api_key
        self.instance_id = instance_id

    def ask(self):
        ask_url = self.url + '/api/ask.json'
        params = { 'api_key' : self.api_key, 'instance' : self.instance_id }
        khepri_ask = urllib.urlopen(ask_url + '?' + urllib.urlencode(params))
        return json.load(khepri_ask)

    def success(self, solution_id):
        success_url = self.url + '/api/success.json'
        params = { 'api_key' : self.api_key, 'instance' : self.instance_id, 'solution' : solution_id }
        khepri_success = urllib.urlopen(success_url + '?' + urllib.urlencode(params))
        return json.load(khepri_success)