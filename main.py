import application_log
import metrics
import time

if __name__ == '__main__':
    metrics.start_metrics_server()  # Start Prometheus metrics server
    while True:
        time.sleep(1)  # Keep the main thread alive
