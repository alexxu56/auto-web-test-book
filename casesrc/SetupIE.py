# -*- coding: utf-8 -*-

import common.ReadConfig as rConfig
from common.IEAction import IEAction
import time
from pymouse import *

class SetupIE():
    def __init__(self):
        pass

    #启动IE并最大化
    def setup_IE(self):
        localreadconfig = rConfig.ReadConfig()
        baseurl = localreadconfig.get_http("baseURL")
        ieaction = IEAction()
        driver = ieaction.setup_IE()
        driver.get(baseurl)
        driver.maximize_window()
        time.sleep(3)
#       ieaction.do_screenshot(driver)
        return driver

    def tear_down(self, driver):
        driver.quit()
"""
if __name__ == "__main__":
    getIE = SetupIE()
    driver = getIE.setup_IE()
    driver.quit()
"""

