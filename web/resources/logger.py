import logging

from amazon.web.drivers.tests_data import TestData


class writeLogs(object):
    def the_logger(self):
        logging.basicConfig(
            filename= TestData.LOGGING_PATH + (__name__)+ ".log",
            level=logging.INFO)

        # logger = logging.getLogger(__name__)
        # logger.setLevel(logging.INFO)
        #
        # # create a file handler
        # handler = logging.FileHandler('reports/logsTest.log')
        # handler.setLevel(logging.DEBUG)
        #
        # # create a logging format
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # handler.setFormatter(formatter)
        #
        # # add the handlers to the logger
        # logger.addHandler(handler)


