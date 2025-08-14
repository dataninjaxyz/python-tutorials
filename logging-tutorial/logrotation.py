import logging
from logging.handlers import RotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    "./logs/app.log",
    maxBytes=2000,
    backupCount=5
)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

print("Writing logs to 'app.log'...")
for i in range(100):
    logger.info(f"This is log message number {i}.")
    time.sleep(0.1)

print("\nLog messages have been written. Check the directory for 'app.log' and its rotated backups.")