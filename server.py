from http.server import BaseHTTPRequestHandler, HTTPServer


class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if(self.path == '/'):
            self.path = '/index.html'
        try:
            file_read = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_read = 'Page not found'
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_read, 'utf-8'))

http_deamon = HTTPServer(('localhost', 7000), WebServer)
http_deamon.serve_forever()