from http.server import BaseHTTPRequestHandler
from urllib import parse
import json
from random import randint
from os.path import join
from tinyhtml import html, h, frag, raw, Frag



class handler(BaseHTTPRequestHandler):

    def layout(self,title:str, message:str):
        return html()(
            h('head')(
                h('title')(title),
                h('link',type='text/css',rel='stylesheet',href='../data/css/style.css')()
            ),
            h('body')(
                h('div',klass='centered')(message)
            )
        ).render()

    def get_html_fortune(self):
        message = self.get_fortune_cookie()
        return self.layout('Be Happy', message)

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

        message = self.get_html_fortune()
        self.wfile.write(message.encode('utf-8'))
        return
