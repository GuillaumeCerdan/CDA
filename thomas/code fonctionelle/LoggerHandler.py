import logging
import datetime

class LogHandler:
    logging.basicConfig(filename='logs.log', filemode='a+', level=logging.DEBUG)
    
    def logger_info(message):
        logging.info(message)

    def logger_debug(message):
        logging.debug(message)

    def logger_warning(message):
        logging.warning(message)

    def logger_error(message):
        logging.error(message)

    def logger_critical(message):
        logging.critical(message)
        

    def get_date():
        return (datetime.datetime.now())
