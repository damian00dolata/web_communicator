# server/logger.py
import logging
import json
from pathlib import Path
import traceback
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage()
        }
        if hasattr(record, "extra_data"):
            log_entry.update(record.extra_data)
        if record.exc_info:
            log_entry["exception"] = "".join(traceback.format_exception(*record.exc_info)).strip()
        return json.dumps(log_entry)

logger = logging.getLogger("web_communicator")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)

def log_info(message: str, **kwargs):
    kwargs = {k: str(v) if isinstance(v, Path) else v for k, v in kwargs.items()}

    logger.info(message, extra={"extra_data": kwargs})

def log_error(message: str, **kwargs):
    kwargs = {k: str(v) if isinstance(v, Path) else v for k, v in kwargs.items()}

    logger.error(message, extra={"extra_data": kwargs})