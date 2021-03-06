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

        return