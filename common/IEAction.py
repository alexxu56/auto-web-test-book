# -*- coding: utf-8 -*-
import os
from datetime import datetime
from selenium import webdriver

selpath = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))

class IEAction():
    def __init__(self):
        pass
#启动IE
    def setup_IE(self):
        try:
            driver = webdriver.Ie()
            return driver
        except Exception, e:
            raise
        finally:
            pass

#抓图
class Screenshot():
    def __init__(self):
        pass

    def do_screenshot(self,driver):
            name = str(datetime.now().strftime("%Y%m%d%H%M%S")) + '.png'
            logpath = os.path.join(selpath, "log/png")
            pngpath = os.path.join(logpath, name)
            print pngpath
            driver.save_screenshot(pngpath)
