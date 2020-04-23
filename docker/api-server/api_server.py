#!/usr/bin/env python

from flask import Flask, request
import requests

import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"

@app.route('/connect/<service>')
def make_connection(service):
    if service == "special":
        url = "http://special:8001/connect"
    elif service == "restricted":
        url = "http://restricted:8002/connect"
    elif service == "external":
        url = "http://external:8003/connect"

    r = requests.get(url, headers=request.headers)
    return r.content, r.status_code

@app.route('/getdata/<service>')
def get_data(service):
    if service == "special":
        url = "http://special:8001/getdata"
    elif service == "restricted":
        url = "http://restricted:8002/getdata"

    r = requests.get(url, headers=request.headers)
    return r.content, r.status_code

if __name__ == "__main__":
    app.run(debug=True)
