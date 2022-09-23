from email import message
from http.server import BaseHTTPRequestHandler
from urllib import parse
import json
from random import randint
from os.path import join



class handler(BaseHTTPRequestHandler):

    def get_fortune_cookie(self):
        with open(join('data','fortune-cookie.json'),'r') as f:
            readed_data = f.read()

        data = json.loads(readed_data)
        data_len = len(data)
        random_position = randint(0, data_len - 1)
        return data[random_position]

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = self.get_fortune_cookie()
        self.wfile.write(message.encode('utf-8'))
        return
