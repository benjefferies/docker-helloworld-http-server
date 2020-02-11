#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)

def start_tcp_server():

    @app.route("/hello")
    def hello():
        return "world"

if __name__ == "__main__":
    start_tcp_server()
    app.run("0.0.0.0", 8080)