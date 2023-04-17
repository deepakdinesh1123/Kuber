import logging
import os

LOG_DIR = "logs"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"


def setup_logging():
    # Create the log directory if it doesn't exist
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    # Configure the logger for info level
    info_logger = logging.getLogger("info")
    info_logger.setLevel(logging.INFO)
    info_handler = logging.FileHandler(os.path.join(LOG_DIR, "info.log"))
    info_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    info_logger.addHandler(info_handler)

    # Configure the logger for debug level
    debug_logger = logging.getLogger("debug")
    debug_logger.setLevel(logging.DEBUG)
    debug_handler = logging.FileHandler(os.path.join(LOG_DIR, "debug.log"))
    debug_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    debug_logger.addHandler(debug_handler)

    # Configure the logger for error level
    error_logger = logging.getLogger("error")
    error_logger.setLevel(logging.ERROR)
    error_handler = logging.FileHandler(os.path.join(LOG_DIR, "error.log"))
    error_handler.setFormatter(logging.Formatter(LOG_FORMAT))
    error_logger.addHandler(error_handler)


def log_info(message):
    logger = logging.getLogger("info")
    logger.info(message)


def log_debug(message):
    logger = logging.getLogger("debug")
    logger.debug(message)


def log_error(message):
    logger = logging.getLogger("error")
    logger.error(message)
