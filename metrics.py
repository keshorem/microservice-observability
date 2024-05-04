from prometheus_client import start_http_server, Summary
import time

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# start the http_server
def start_metrics_server(port=8000):
    start_http_server(port)
