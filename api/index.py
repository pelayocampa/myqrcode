from http.server import BaseHTTPRequestHandler
from urllib import parse
import json
from random import randint



class handler(BaseHTTPRequestHandler):

    def get_fortune_cookie():
        with open('./fortune-cookie.json') as f:
            readed_data = f.read()

        data = json.loads(readed_data)
        data_len = len(data)
        random_position = randint(0, data_len - 1)
        return data[random_position]


    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        message = "Test me: "+self.get_fortune_cookie()
        self.wfile.write(message.encode())
        return
