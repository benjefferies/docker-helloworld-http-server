#!/usr/bin/env python
import json
from flask import Flask, request

app = Flask(__name__)

def start_tcp_server():

    @app.route("/hello")
    def hello():
        response = {}
        response["headers"] = dict(request.headers)
        response["request"] = dict(request.data)
        return json.dumps(response, sort_keys=True, indent=4)

if __name__ == "__main__":
    start_tcp_server()
    app.run("0.0.0.0", 8080)