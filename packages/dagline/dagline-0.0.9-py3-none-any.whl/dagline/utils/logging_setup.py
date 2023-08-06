import logging
import sys
from logging import Logger


class TaskLogFilter(logging.Filter):
    def filter(rec : logging.LogRecord):
        if (rec.getMessage().startswith("Output---From---Task")):
            return False
        else:
            return True
        
        
        
class LoggingMixin:
    _log: logging.Logger = None
    
    @property
    def log(self) -> Logger:
        """Returns a logger."""
        if self._log is None:
            log_formater = logging.Formatter('[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s')
            stdout_handler = logging.StreamHandler(sys.stdout)
            stdout_handler.setFormatter(log_formater)
            self._log = logging.getLogger(self.__class__.__module__ + "." + self.__class__.__name__)
            self._log.addHandler(stdout_handler)
            stdout_handler.addFilter(TaskLogFilter)
            '''Use the log file that was provided by the module'''
            if hasattr(self, 'logfile'):
                logfile_handler = logging.FileHandler(self.logfile)
                logfile_handler.setFormatter(log_formater)
                self._log.addHandler(logfile_handler)
            self._log.setLevel(logging.DEBUG)
        return self._log

    @classmethod
    def getLogger(cls, log_name) -> Logger:
        # log_format = (
            # '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s')

        # logging.basicConfig(
            # level=logging.DEBUG,
            # format=log_format,
            # handlers=[
                # logging.StreamHandler(sys.stdout)
            # ]
        # )
        log_formater = logging.Formatter('[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s')
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(log_formater)
        logger = logging.getLogger(log_name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(stdout_handler)
        return logger


