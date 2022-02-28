import logging

# CASE 1 -----> Error Type Known
# try:
#     a = [1,2]
#     print(a[9])
# except IndexError as e:
#     logging.error(e, exc_info=True)

# CASE 2 ------> Error Type Not Known and want TRACEBACK
import traceback
try:
    a = 5/0
except:
    logging.error('The error is %s', traceback.format_exc())