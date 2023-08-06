from logging import getLogger, basicConfig, StreamHandler, DEBUG, INFO
from sys import stdout


class HandlerLog():
    def __init__(self):
        basicConfig(filename='debug.log', filemode='a', format='%(name)s - %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level='DEBUG')

        basicConfig(filename='info.log', filemode='a', format='%(name)s - %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level='INFO')

        self.log = self.get_log()

    def get_log(self, log_name="AcodisAPIHandler"):
        log = getLogger(log_name)
        log.addHandler(StreamHandler(stream=stdout))
        self.log = log
        return log
