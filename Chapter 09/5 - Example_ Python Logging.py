import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)

def my_function():
    logging.debug('This is a debug message')
    logging.info('Some   
 information')
    logging.warning('A warning occurred')
    logging.error('An error happened')

try:
    # Some code that might raise an exception
    my_function()
    result = 10 / 0 # Will raise ZeroDivisionError
except Exception as e:
    logging.exception("An exception occurred: %s", e)
