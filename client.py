import requests
import base64
import sys
import json

class AClient(object):
    __module__       = 'aes-service/client.py'
    __author__       = 'Rob Mitchell'
    __maintainer__   = 'Rob Mitchell'
    __email__        = 'rlmitchell@gmail.com'
    __version__      = '1.0.0'
    __version_date__ = '2020.06.06.1753ct'
    __status__       = 'personal use release'

    def __init__(self, filename, service_endpoint=None):
        if not service_endpoint:
            self.service_endpoint = 'http://localhost:6000/process'
        else:
            self.service_endpoint = service_endpoint
        self.data = self.load_file(filename)
        self.payload = {}

    def load_file(self,filename):
        with open(filename,'rb') as f:
            return f.read()

    def __call__(self,action):
        self.payload['action'] = action
        self.payload['text'] = base64.b64encode(self.data)
        resp = requests.post(self.service_endpoint, json=self.payload)
        sys.stderr.write( resp.code )
        sys.stdout.write( base64.b64decode( resp.json()['text'] ) )


if __name__ == '__main__':
    AClient(sys.argv[1])(sys.argv[2])

