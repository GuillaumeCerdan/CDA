import logging
import datetime


class LogHandler:

    logging.basicConfig(filename='logs.log', filemode='a+', level=logging.DEBUG)

    def logger_info(message):
        """
        metode qui permet de logger des message d'iportance info
        -------------------------------------------------------
        message = message à logger
        -------------------------------------------------------
        """
        logging.info(message)

    def logger_debug(message):
        """
        metode qui permet de logger des message d'iportance debug
        -------------------------------------------------------
        message = message à logger
        -------------------------------------------------------
        """
        logging.debug(message)

    def logger_warning(message):
        """
        metode qui permet de logger des message d'iportance warning
        -------------------------------------------------------
        message = message à logger
        -------------------------------------------------------
        """
        logging.warning(message)

    def logger_error(message):
        """
        metode qui permet de logger des message d'iportance error
        -------------------------------------------------------
        message = message à logger
        -------------------------------------------------------
        """
        logging.error(message)

    def logger_critical(message):
        """
        metode qui permet de logger des message d'iportance critical
        -------------------------------------------------------
        message = message à logger
        -------------------------------------------------------
        """
        logging.critical(message)

    def get_date():
        return (datetime.datetime.now())
