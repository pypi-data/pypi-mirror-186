"""
Logging基础库

Title:
    logging_util

Author:
    rzzhou

#我吉良吉影只想过平静的生活

Functions:
1.继承loguru的日志打印
2.如果设置路径则产生日志文件,无路径则无文件、

"""
import logging
import sys
import time
from os import makedirs
from os.path import dirname, exists

class LoggingUtil(object):
    def __init__(self,
                 mode: str = "MODE_SIMPLE_DEV",
                 logfile: str = None):

        """
        初始化Logging工具

        Args:
            mode: 1. MODE_DEV
                  2. MODE_PROD
                  3. MODE_SIMPLE_DEV
            logfile: 1. PATH+FILE
                     2. None
        """
        global loggers
        loggers = {}

        self.logger = logging.getLogger(__name__)#从logging 中直接取出logger
        # 是否开启日志
        self.LOG_ENABLED = True
        # 是否输出到控制台
        self.LOG_TO_CONSOLE = True
        # 是否输出到文件
        self.LOG_TO_FILE = True

        self.LOG_FORMAT = "%(asctime)s - %(levelname)s - process:%(process)d - %(filename)s - " \
                          "%(name)s - %(lineno)d - %(module)s - %(message)s"

        if mode == "MODE_DEV":
            self.default_log_file = logfile if logfile is not None else None
            self.LOG_LEVEL = "DEBUG"
            self.logger.setLevel(self.LOG_LEVEL)
            self._add_logfile(filepath=logfile,
                              level=self.LOG_LEVEL)

        elif mode == "MODE_PROD":
            self.default_log_file = logfile if logfile is not None else None
            self.LOG_LEVEL = "INFO"
            self.logger.setLevel(self.LOG_LEVEL)
            self._add_logfile(filepath=logfile,
                              level=self.LOG_LEVEL)

        elif mode == "MODE_SIMPLE_DEV":
            self.LOG_TO_FILE = False
            self.LOG_LEVEL = "DEBUG"
            self.logger.setLevel(self.LOG_LEVEL)

        else:
            raise Exception("MODE_ERROR")

        self._add_logconsole()


    def _add_logconsole(self):
        """
        私有: 建立控制台输出句柄

        Returns:
            无
        """
        #   输出到控制台
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(level=self.LOG_LEVEL)
        formatter = logging.Formatter(self.LOG_FORMAT)
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)


    def _add_logfile(self,
                     filepath: str = None,
                     level: str = None):

        """
        私有:设置日志文件目标与参数

        Args:
            filepath: 日志文件路径
            level: 日志等级

        Returns:
        """
        t = time.strftime("%Y%m%d%H%M")
        # 日志文件路径
        self.LOG_PATH = "./logs/"+t+".log" if filepath is None else filepath
        # 日志级别
        self.LOG_LEVEL = "INFO" if level is None else level

        log_dir = dirname(self.LOG_PATH)
        if not exists(log_dir): makedirs(log_dir)
        # 添加FileHandler
        file_handler = logging.FileHandler(self.LOG_PATH, encoding='utf-8')
        file_handler.setLevel(level=self.LOG_LEVEL)
        formatter = logging.Formatter(self.LOG_FORMAT)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        logger_name = self.logger
        loggers[logger_name] = self.logger
        return self.logger


    def _get_logger(self, name=None):
        '''
        get logger by name
        :param name: name or logger
        :return: logger
        '''

        global loggers

        if not name: name = __name__
        if loggers.get(name):
            return loggers.get(name)

        logger = logging.getLogger(name)

        #   输出到控文件
        if self.LOG_ENABLED and self.LOG_TO_FILE:
            # 如果路径不存在,创建
            log_dir = dirname(self.LOG_PATH)
            if not exists(log_dir): makedirs(log_dir)
            # 添加FileHandler
            file_handler = logging.FileHandler(self.LOG_PATH, encoding='utf-8')
            file_handler.setLevel(level=self.LOG_LEVEL)
            formatter = logging.Formatter(self.LOG_FORMAT)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        #    保存到全局loggers
        loggers[name] = logger
        return logger

    def debug(self,msg):
        """
        调用logger打印debug级别日志，如果有日志文件会写进日志文件

        Args:
            msg(str): 打印字符串

        Returns:
            无返回

        Returns:

        """
        self.logger.debug(msg)


    def info(self,msg):
        """
        调用logger打印info级别日志，如果有日志文件会写进日志文件

        Args:
            msg(str): 打印字符串

        Returns:
            无返回
        """
        self.logger.info(msg)

    def warning(self,msg):
        """
        调用logger打印warning级别日志，如果有日志文件会写进日志文件

        Args:
            msg(str): 打印字符串

        Returns:
            无返回
        """
        self.logger.warning(msg)

    def error(self,msg):
        """
        调用logger打印error级别日志，如果有日志文件会写进日志文件

        Args:
            msg(str): 打印字符串

        Returns:
            无返回
        """
        self.logger.error(msg)



# if __name__ == "__main__":
#     logger.debug("this is a meaage...")
#     logger.error("this is a error...")

