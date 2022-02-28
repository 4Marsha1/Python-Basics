import logging

# Create Logger
logger = logging.getLogger(__name__)

# Create log Handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.txt')

# Setting Log Handler
# 1. Setting level
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

# 2. Setting formatter
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

# ADDING log Handlers to logger
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning')
logger.error('This is an error')