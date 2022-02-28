import logging

# 1. ROTATING FILE HANDLER
# from logging.handlers import RotatingFileHandler
#
# # CREATE LOGGER----> Set Level ----> Add Handler ---> Trigger
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
#
# handler = RotatingFileHandler('app.log', maxBytes=3000, backupCount=5)
# logger.addHandler(handler)
#
# for _ in range(15000):
#     logger.info('Hello World!')

# 3. TIMED ROTATING FILE HANDLER
from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s, m, h, d, midnight, w0, w1 ....
handler = TimedRotatingFileHandler('test_log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Hello')
    time.sleep(5)