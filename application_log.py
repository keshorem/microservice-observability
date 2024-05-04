import time
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename='process_logs.log')
logger = logging.getLogger(__name__)

time_end = time.time() + 60 * 1

while time.time() < time_end:
    logger.info("processing logs")




