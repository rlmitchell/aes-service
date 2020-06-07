import cherrypy
import base64 
import json
import requests
from cherrypy import tools

from config import Config
from aesutil import AESUtil

class App(object):
    __module__       = 'aes-service/app.py'
    __author__       = 'Rob Mitchell'
    __maintainer__   = 'Rob Mitchell'
    __email__        = 'rlmitchell@gmail.com'
    __version__      = '1.0.0'
    __version_date__ = '2020.06.06.1657ct'
    __status__       = 'personal use release'

    def __init__(self):
        self.config = Config.get_parser('app.ini')
        aes = AESUtil(self.getkey())

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def process(self):
        json_in = cherrypy.request.json
        json_in['text'] = base64.b64decode(json_in['text'])
        json_out = {}
        json_out['version'] = self.version

        if json_in['action'] == 'encrypt':
            json_out['text'] = base64.b64encode(aes.encrypt(json_in['text']))
        else:
            json_out['text'] = base64.b64encode(aes.decrypt(json_in['text']))
        return json_out

    def getkey(self):
        return requests.get(self.config['KeyService']['url']+'/'+self.config['KeyService']['key']).content.rstrip()
		


if __name__ == '__main__':
    parser = Config.get_parser('app.ini')
    conf = {
        'server.socket_host':str(parser['App']['host']),
        'server.socket_port':int(parser['App']['port']),
        'server.max_request_body_size' : 0,
        'server.socket_timeout' : 120,
        'server.thread_pool':int(parser['App']['threads'])
    }
    cherrypy.config.update(conf)
    cherrypy.quickstart(App())

