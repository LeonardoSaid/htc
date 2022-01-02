import os
import logging
from logging.config import fileConfig

API_VERSION = "v1"
BASE_PATH = f"/cart-management/{API_VERSION}"
BLACK_FRIDAY_DATE = "02/01/2022"

DISCOUNT_SERVICE_HOST = os.environ.get("DISCOUNT_SERVICE_HOST", "discount:50051")
SERVICE_HOST = os.environ.get("SERVICE_HOST", "0.0.0.0")
SERVICE_PORT = os.environ.get("SERVICE_PORT", 8000)

fileConfig("src/config/logging_config.ini")
LOGGER = logging.getLogger("sLogger")
