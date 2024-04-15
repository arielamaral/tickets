import os
import time
from flask import Flask, request, jsonify, g

def after_request_callable(response):
    diff = (time.time() - g.start)
    Metric_Logger().log_event_endpoint(request.method, request.endpoint, diff, response.status_code)
    return response
def handle_error():
    diff = (time.time() - g.start)
    Metric_Logger().log_event_endpoint(request.method, request.endpoint, diff, 500, 1)
    return execption

def before_request():
    g.start = time.time()

def create_app():
    app = Flask(__name__)
    app.before_request(before_request)
    app.after_request(after_request_callable)