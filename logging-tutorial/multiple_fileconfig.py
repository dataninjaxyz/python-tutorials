import logging
import logging.config

logging.config.fileConfig('multi_logging.conf')

logger = logging.getLogger('multiLogger')

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
