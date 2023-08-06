"""
Loguru基础库

Title:
    loguru_util

Author:
    rzzhou

#我吉良吉影只想过平静的生活

Functions:
1.初始化预设模板
2.工具直接实现多个打印: debug info warning error
3.修改日志文件的参数

"""

from loguru import logger
import sys
import time


class LoguruUtil:
    def __init__(self,
                 mode: str = "MODE_SIMPLE_DEV",
                 logfile: str = None
                 ):
        """
        初始化Loguru工具

        Args:
            mode: 1. MODE_DEV
                  2. MODE_PROD
                  3. MODE_SIMPLE_DEV
            logfile: 1. PATH+FILE
                     2. None
        """

        self.logger = logger

        self.default_handler_id = None

        self.default_log_file = None
        if mode == "MODE_DEV":
            self.default_log_file = logfile if logfile is not None else None
            self.default_handler_id = self._add_sink(sink=self.default_log_file,
                                                        level="DEBUG")
        elif mode == "MODE_PROD":
            self.default_log_file = logfile if logfile is not None else None
            self.default_handler_id = self._add_sink(sink=self.default_log_file,
                                                     level="INFO")
        elif mode == "MODE_SIMPLE_DEV":
            pass
        else:
            raise Exception("MODE_ERROR")

    def _add_sink(self,
                sink: str = None,
                level: str = None
                ):
        """
        私有:设置日志文件目标与参

        Args:
            sink(str): 日志文件句柄
            level(dict): 日志文件记录的最低等级

        Returns:
            handler id
        """
        t = time.strftime("%Y%m%d%H%M")
        new_sink = "./logs/"+ t + ".log" if sink is None else sink
        new_level = "INFO" if level is None else level

        hander_id = self.logger.add(sink=f"{new_sink}",
                                    level=new_level,
                                    encoding="utf-8",
                                    enqueue=True)
        return hander_id

    def info(self, msg):
        """
        调用logger打印info级别日志，如果有日志文件会写进日志文件

        Args:
            msg(str): 打印字符串

        Returns:
            无返回
        """
        self.logger.info(msg)

    def debug(self, msg):
        """
        调用logger打印debug级别日志，如果有日志文件会写进日志文件

        Args:
            msg(str):打印字符串

        Returns:
            无返回
        """
        self.logger.debug(msg)

    def warning(self, msg):
        """
        调用logger打印warning级别日志，如果有日志文件会写进日志文件

        Args:
            msg(str):打印字符串

        Returns:
            无返回
        """
        self.logger.warning(msg)

    def error(self, msg):
        """
        调用logger打印error级别日志，如果有日志文件会写进日志文件

        Args:
            msg(str):打印字符串

        Returns:
            无返回
        """
        self.logger.error(msg)

    def success(self,msg):
        """
        调用logger打印success级别日志，如果有日志文件会写进日志文件

        Args:
            msg:

        Returns:
            无返回
        """
        self.logger.success(msg)


    # def add_logfile(self,
    #                 logfile: str = None,
    #                 level: str = "INFO",
    #                 format: str = None,
    #                 enqueue: bool = True,
    #                 encoding: str = "utf-8"
    #                 ):



    def configure_default_logfile(self,
                                  logfile: str = None,
                                  level: str = "INFO",
                                  format: str = None,
                                  enqueue: bool = True
                                  ):

        """
        配置默认的日志文件

        Args:
            logfile(str): 日志文件路径,如果不存在默认的日志文件则以该文件
            level(str): 日志文件最低显示级别, 默认为INFO
            format(str): 日志文件中的显示的格式,如不填则为默认
            enqueue(str): 日志文件是否连续写

        Returns:
            无返回
        """
        t = time.strftime("%Y%m%d%H%M")
        logfile = "./logs/"+ t + ".log" if logfile is None else logfile

        logfile_handler_dict ={
            "sink": logfile,
            "level": level,
            "enqueue": enqueue
        }
        if format is not None:
            logfile_handler_dict["format"] = format
        if self.default_handler_id is not None:
            self.logger.remove(self.default_handler_id)

            if logfile == self.default_log_file:
                self.default_handler_id = self.logger.add(**logfile_handler_dict)#**转换
            else:
                self.default_handler_id =self.logger.add(**logfile_handler_dict)

        else:
            self.default_handler_id = self.logger.add(**logfile_handler_dict)


if __name__ == '__main__':

    log_util = LoguruUtil()
    log_util.info("This is info log")
    log_util.debug("this is debug log")
    log_util.warning("this is a warning")
    log_util.error("error error error")

    """
    log_util_f1 = LoguruUtil(mode="MODE_DEV", logfile="D:\\Workspace\\2021022401.log")
    log_util_f1.info("This is info log")
    log_util_f1.debug("this is debug log")
    log_util_f1.warning("this is a warning")
    log_util_f1.error("error error error")

    # log_util_err = LoguruUtil(MODE="err")
 
    log_util_f2 = LoguruUtil(mode="MODE_PROD", logfile="D:\\Workspace\\2021022401P.log")
    log_util_f2.info("This is info log")
    log_util_f2.debug("this is debug log")
    log_util_f2.warning("this is a warning")
    log_util_f2.error("error error error")
    """

    log_util_o1 = LoguruUtil(mode="MODE_DEV", logfile = "D:\\change_log_file.log")

    log_util_o1.info("info success!")

    log_util_o1.configure_logfile(logfile = "D:\\change_log_file.log")

    log_util_o1.error("changed!")






