import logging

# LOGGER CONFIG
logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

# BY DEFAULT: Only warning onwards gets logged in OUTPUT
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
logging.error('This is error message')
logging.critical('This is critical message')

import __helper