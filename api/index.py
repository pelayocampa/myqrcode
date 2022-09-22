from http.server import BaseHTTPRequestHandler
from urllib import parse
import json
from random import randint

url = "https://raw.githubusercontent.com/reggi/fortune-cookie/master/fortune-cookie.json"

class handler(BaseHTTPRequestHandler):

    def get_fortune_cookie():
        file = open("fortune-cookie.json", "r")
        data = json.loads(file)
        data_len = len(data)
        random_position = randint(0, data_len - 1)
        file.close()
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
