# import http.server
# import socketserver
import json
#
# # from controller import blockColor, rgb
#
#
# class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
#     def do_GET(self):
#         if self.path == '/':
#             self.path = 'index.html'
#         return http.server.SimpleHTTPRequestHandler.do_GET(self)
#
#     def log_message(self, format, *args):
#         return
#
#     def do_POST(self):
#         data_string = self.rfile.read(int(self.headers['Content-Length']))
#
#         data = json.loads(data_string)
#         print(data)
#         # blockColor(rgb(data['color']))
#
#         self.send_response(http.server.HTTPStatus.OK)
#         return self.end_headers()
#
#
# if __name__ == '__main__':
#     # Create an object of the above class
#     handler_object = MyHttpRequestHandler
#
#     PORT = 8000
#     my_server = socketserver.TCPServer(("", PORT), handler_object)
#
#     # Start the server
#     my_server.serve_forever()


from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='',static_folder='public', template_folder='public')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/color", methods=['POST'])
def handleColor():
    print("Recieved Post")
    data = request.get_data().decode()
    data = json.loads(data)
    color = data['color']
    print(color)
    return "Success"