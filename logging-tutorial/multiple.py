import logging
from logging.config import dictConfig

logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'console_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'INFO',  # onsole_handler only shows INFO and higher
        },
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'formatter': 'standard',
            'level': 'DEBUG', # file_handler shows everything
        },
    },
    'loggers': {
        'myapp': {
            'handlers': ['console_handler', 'file_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

dictConfig(logging_config)
logger = logging.getLogger('myapp')

logger.debug("This will only appear in the file.")
logger.info("This will appear in both the console and the file.")