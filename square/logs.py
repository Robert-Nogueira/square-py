import logging

# logging config
logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)

class CustomFormatter(logging.Formatter):
    """a custom logging formatter"""
    green = '\033[0;32m'
    yellow = '\033[0;33m'
    red = '\033[0;31m'
    end = '\033[m'

    FORMAT = ' %(levelname)s:  [%(id)s] %(message)s'

    FORMATS = {
        logging.INFO: green + FORMAT + end,
        logging.DEBUG: yellow + FORMAT + end,
        logging.ERROR: red + FORMAT + end
    }
    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

# console handler
_ch = logging.StreamHandler()
_ch.setLevel(logging.INFO)
_ch.setFormatter(CustomFormatter())
logger.addHandler(_ch)
