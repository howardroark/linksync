from flask import Flask
from flask_sockets import Sockets
import os

app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/<hash>')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        ws.send(message)

@app.route('/')
def index():
    return 'linksync'
