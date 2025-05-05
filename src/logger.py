import logging
import os
from datetime import datetime

# Folder for storing logs
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Dynamic log filename based on current date and time
LOG_FILE = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

# Basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # Show logs in terminal too
    ]
)

# Logger object to be imported anywhere
logger = logging.getLogger("mlprojects_logger")


