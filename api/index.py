from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):

  def _set_headers(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

  def do_HEAD(self):
    self._set_headers()

  def do_GET(self):
    self._set_headers()

    message = "Hello"

    dow = {'change': 100, 'percentChange': 2.3234, 'price': 23145.231}
    nasdaq = {'change': -100, 'percentChange': -2.3234, 'price': 321235.232}
    sp500 = {'change': 232, 'percentChange': 4.3234, 'price': 1223.23}

    json_string = json.dumps({'dow': dow, 'nasdaq': nasdaq, 'sp500': sp500})
    self.wfile.write(json_string.encode(encoding='utf_8'))
    return
