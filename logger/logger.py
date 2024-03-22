import logging
from logging.handlers import TimedRotatingFileHandler

logging.basicConfig(
    format='%(asctime)s => %(message)s'
)

def create_logger(service_name: str, path: str):
    rotatingHandlerLog = TimedRotatingFileHandler(path, when="d", interval=1, backupCount=5)

    rotatingHandlerLog.setFormatter(logging.Formatter(
        '%(asctime)s [' + service_name.replace(' ', '_') + ']::[%(levelname)s] => %(message)s'
    ))
    log = logging.getLogger(service_name)
    log.addHandler(rotatingHandlerLog)

    return log