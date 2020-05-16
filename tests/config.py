import os
import logging

# Set log level for all unit tests
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

API_KEY = os.environ.get("SALESFLY_APIKEY")
