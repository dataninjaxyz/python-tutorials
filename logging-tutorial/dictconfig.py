import logging
from logging.config import dictConfig

# A logging configuration
logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - [%(levelname)s] - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'demo': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
    }
}

dictConfig(logging_config)

logger = logging.getLogger('demo')
logger.info("This is an informational message from my_app.")
logger.debug("This is a debug message from my_app.")