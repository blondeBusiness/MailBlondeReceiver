from enum import StrEnum
import logging

class LogLevels(StrEnum):
    info = "INFO"
    warn = "WARN"
    error = "ERROR"
    debug = "DEBUG"

# Definir formatos de log (esto probablemente falta en tu código)
LOG_FORMAT_DEBUG = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FORMAT_DEFAULT = '%(levelname)s - %(message)s'

def configure_logging(log_level: str = LogLevels.error):
    log_level = str(log_level).upper()
    log_levels = [level.value for level in LogLevels]

    if log_level not in log_levels:
        logging.basicConfig(level=LogLevels.error)
        return

    if log_level == LogLevels.debug:
        logging.basicConfig(level=log_level, format=LOG_FORMAT_DEBUG)
        return

    logging.basicConfig(level=log_level)