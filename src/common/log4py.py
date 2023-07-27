import logging

from colorlog import ColoredFormatter

from src.common.const import *

LOG_LEVEL = logging.DEBUG

LOGFORMAT = "  %(log_color)s%(asctime)s  %(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
logging.root.setLevel(LOG_LEVEL)
logFormatter = ColoredFormatter(LOGFORMAT)

rootLogger = logging.getLogger()

fileHandler = logging.FileHandler(f"./{APP_NAME}.log")
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

_logger = None


def get_logger():
	global _logger
	if not _logger:
		_logger = logging.getLogger()
		_logger.setLevel(logging.DEBUG)
	return _logger
