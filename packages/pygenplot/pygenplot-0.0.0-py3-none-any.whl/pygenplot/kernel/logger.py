import logging

_levels = {
    "critical" : logging.CRITICAL,
    "debug" : logging.DEBUG,
    "error" : logging.ERROR,
    "fatal" : logging.FATAL,
    "info" : logging.INFO,
    "warning" : logging.WARNING}

LOGGER = {}

LOGGER["main"] = logging.getLogger("main")
LOGGER["popup"] = logging.getLogger("popup")

def log(message,loggers,level):
    for logger in loggers:
        LOGGER[logger].log(_levels[level],message)



