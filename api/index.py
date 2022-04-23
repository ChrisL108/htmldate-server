from http.server import BaseHTTPRequestHandler
from htmldate import find_date
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        query_params =  urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        url = query_params.get('url')[0]
        publish_date = find_date(url, original_date=True) # outputformat='%Y-%m-%dT%H:%M:%S%z'
        self.wfile.write(publish_date.encode())

        # # WORKING
        # query_params =  urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        # self.wfile.write(json.dumps(query_params, separators=(',', ':')).encode())
        # # result = {"url":["http://gawker.com/men-dressed-as-ninjas-rob-millionaire-and-companion-in-1570983668"]}

        
        # WORKING
        # self.wfile.write(json.dumps(urllib.parse.parse_qs(self.path), separators=(',', ':')).encode())
        # result = {"/api?url":["http://gawker.com/men-dressed-as-ninjas-rob-millionaire-and-companion-in-1570983668"]}
        return