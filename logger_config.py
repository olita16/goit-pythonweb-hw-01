# logger_config.py
import logging

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
