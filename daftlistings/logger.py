import logging


class Logger(object):

    def __init__(self, level=logging.ERROR):
        logging.basicConfig(level=level)
        self.logger = logging.getLogger(__name__)

    def info(self, message):
        return self.logger.info(message)

    def error(self, message):
        return self.logger.error(message)
