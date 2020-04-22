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
        status_code = request.args.get('status_code')
        if not status_code.isnumeric():
            status_code = 200
        return json.dumps(response, sort_keys=True, indent=4), status_code

if __name__ == "__main__":
    start_tcp_server()
    app.run("0.0.0.0", 8080)