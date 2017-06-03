from flask import Flask
from flask_sockets import Sockets
import os


app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/ws')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        ws.send(message)


@app.route('/')
def index():
    return 'linksync'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', os.environ.get('PORT')), app, handler_class=WebSocketHandler)
    server.serve_forever()
