# -*- coding:UTF-8 -*-
"""
TITLE: 'test_loguru_util'
AUTHOR: 'rzzhou'
MTIME = '2021/03/01'
#我吉良吉影只想过平静的生活
"""
import os
import unittest
import time
from halring.log.loguru_util import LoguruUtil

class TestLoguruUtil(unittest.TestCase):
    def test_loguru_util_001_debug(self):
        loguru_util = LoguruUtil()
        msg = "debug msg"
        loguru_util.debug(msg)

    def test_loguru_util_002_info(self):
        loguru_util = LoguruUtil()
        msg = "info msg"
        loguru_util.info(msg)

    def test_loguru_util_003_warning(self):
        loguru_util = LoguruUtil()
        msg = "warning msg"
        loguru_util.warning(msg)

    def test_loguru_util_004_error(self):
        loguru_util = LoguruUtil()
        msg = "error msg"
        loguru_util.error(msg)

    def test_loguru_util_005_success(self):
        loguru_util = LoguruUtil()
        msg = "success msg"
        loguru_util.success(msg)

    def test_loguru_util_006_MODE_DEV_001(self):
        loguru_util = LoguruUtil("MODE_DEV")
        msg = "MODE DEV MSG"
        loguru_util.debug(msg)
        loguru_util.info(msg)

    def test_loguru_util_007_MODE_DEV_002(self):
        t = time.strftime("%Y%m%d%H%M%S")
        log_path = os.path.abspath(__file__).split(__name__)[0] + "loguru_unittest_" + t + ".log"
        loguru_util = LoguruUtil("MODE_DEV", log_path)
        loguru_util.debug("this is a debug msg")
        loguru_util.info("this is a info msg")
        loguru_util.warning("this is a warning msg")
        loguru_util.error("this is a error msg")
        loguru_util.success("this is a success msg")

    def test_logging_util_008_MODE_PROD_001(self):
        loguru_util = LoguruUtil("MODE_PROD")
        msg = "MODE PROD MSG"
        loguru_util.debug(msg)
        loguru_util.info(msg)

    def test_loguru_util_009_MODE_PROD_002(self):
        t = time.strftime("%Y%m%d%H%M%S")
        log_path = os.path.abspath(__file__).split(__file__)[0] + "loguru_unittest_" + t + ".log"
        loguru_util = LoguruUtil("MODE_PROD", log_path)
        loguru_util.debug("this is a debug msg")
        loguru_util.info("this is a info msg")
        loguru_util.warning("this is a warning msg")
        loguru_util.error("this is a error msg")
        loguru_util.success("this is a success msg")

    def test_loguru_util_010_CONFIGURATION_001(self):
        loguru_util = LoguruUtil()
        loguru_util.configure_default_logfile()
        loguru_util.debug("this is a debug msg")
        loguru_util.info("this is a info msg")
        loguru_util.warning("this is a warning msg")
        loguru_util.error("this is a error msg")
        loguru_util.success("this is a success msg")

    def test_loguru_util_011_CONFIGURATION_002(self):

        loguru_util = LoguruUtil(mode="MODE_DEV")
        loguru_util.configure_default_logfile()
        loguru_util.debug("this is a debug msg")
        loguru_util.info("this is a info msg")
        loguru_util.warning("this is a warning msg")
        loguru_util.error("this is a error msg")
        loguru_util.success("this is a success msg")

    def test_loguru_util_012_CONFIGURATION_003(self):
        t = time.strftime("%Y%m%d%H%M%S")
        log_path = os.path.abspath(__file__).split(__file__)[0] + "loguru_unittest_" + t + ".log"
        loguru_util = LoguruUtil(mode="MODE_DEV")
        loguru_util.debug("this is a debug msg")
        loguru_util.info("this is a info msg")
        loguru_util.warning("this is a warning msg")
        loguru_util.error("this is a error msg")
        loguru_util.success("this is a success msg")
        loguru_util.configure_default_logfile(logfile=log_path)
        loguru_util.debug("this is a debug msg")
        loguru_util.info("this is a info msg")
        loguru_util.warning("this is a warning msg")
        loguru_util.error("this is a error msg")
        loguru_util.success("this is a success msg")
