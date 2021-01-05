import http.server
import socketserver
import json

from controller import blockColor, rgb


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def log_message(self, format, *args):
        return

    def do_POST(self):
        data_string = self.rfile.read(int(self.headers['Content-Length']))

        data = json.loads(data_string)
        blockColor(rgb(data['color']))

        self.send_response(http.server.HTTPStatus.OK)
        return self.end_headers()


if __name__ == '__main__':
    # Create an object of the above class
    handler_object = MyHttpRequestHandler

    PORT = 8000
    my_server = socketserver.TCPServer(("", PORT), handler_object)

    # Start the server
    my_server.serve_forever()
