from flask import Flask, render_template
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
    return render_template('index.html')
