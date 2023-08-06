# -*— coding:UTF-8 -*-
"""
TITLE: 'test_logging_util'
AUTHOR: 'rzzhou'
MTIME = '2021/03/02'
"""
import os
import unittest
import time
from halring.log.logging_util import LoggingUtil

class TestLoggingUtil(unittest.TestCase):
    def test_logging_util_001_debug(self):
        logging_util = LoggingUtil()
        msg = "debug msg"
        logging_util.debug(msg)

    def test_logging_util_002_info(self):
        logging_util = LoggingUtil()
        msg = "info msg"
        logging_util.info(msg)

    def test_logging_util_003_warning(self):
        logging_util = LoggingUtil()
        msg = "warning msg"
        logging_util.warning(msg)

    def test_logging_util_004_error(self):
        logging_util = LoggingUtil()
        msg = "error msg"
        logging_util.error(msg)

    def test_logging_util_005_MODE_DEV_001(self):
        logging_util = LoggingUtil(mode="MODE_DEV")
        logging_util.debug("this is a debug msg")
        logging_util.info("this is a info msg")
        logging_util.warning("this is a warning msg")
        logging_util.error("this is a error msg")

    def test_logging_util_006_MODE_DEV_002(self):
        t = time.strftime("%Y%m%d%H%M%S")

        log_path = os.path.abspath(__file__).split(__name__)[0] + "loging_unittest_" + t + ".log"
        logging_util = LoggingUtil(mode="MODE_DEV",logfile=log_path)
        logging_util.debug("this is a debug msg")
        logging_util.info("this is a info msg")
        logging_util.warning("this is a warning msg")
        logging_util.error("this is a error msg")

    def test_logging_util_007_MODE_PROD_001(self):
        logging_util = LoggingUtil(mode="MODE_PROD")
        logging_util.debug("this is a debug msg")
        logging_util.info("this is a info msg")
        logging_util.warning("this is a warning msg")
        logging_util.error("this is a error msg")

    def test_logging_util_008_MODE_PROD_002(self):

        t = time.strftime("%Y%m%d%H%M%S")
        log_path = os.path.abspath(__file__).split(__name__)[0] + "loging_unittest_" + t + ".log"
        logging_util = LoggingUtil(mode="MODE_PROD",logfile=log_path)
        logging_util.debug("this is a debug msg")
        logging_util.info("this is a info msg")
        logging_util.warning("this is a warning msg")
        logging_util.error("this is a error msg")