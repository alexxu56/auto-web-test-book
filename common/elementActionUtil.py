# -*- coding: utf-8 -*-
import time
import ReadConfig as rConfig
from pymouse import *

class ElementAction():
    def __init__(self):
        pass

    def singleclick(self, webdriver, elementname='', method='Id'):
        'method value:Id,Name,Class,xpath;webdriver value Firefox,Ie'
        waitforele = waitforElementPresentAction()
        element1 = waitforele.waitforElementPresentAction(webdriver, elementname, method)
        element1.click()

    #定位单击鼠标
    def singleclickpos(self,webdriver,elementname='',method='Id'):
        waitforele = waitforElementPresentAction()
        element1 = waitforele.waitforElementPresentAction(webdriver, elementname, method)
        location1 = element1.location
        # 60 偏移量
        y = int(location1['y'])+60
        x = int(location1['x'])-50
        mymouse = PyMouse()
        mymouse.move(x, y)
        time.sleep(1)
        mymouse.click(x,y,1)
        time.sleep(1)

    def selectbook(self,webdriver,elementname='',method='Id'):
        waitforele = waitforElementPresentAction()
        element1 = waitforele.waitforElementPresentAction(webdriver, elementname, method)
        location1 = element1.location
        # 45 偏移量
        y = int(location1['y'])-10
        x = int(location1['x'])
        mymouse = PyMouse()
        mymouse.move(x, y)
        time.sleep(1)
        mymouse.click(x,y,1)
        time.sleep(1)

    def actionbook(self,webdriver,elementname='',method='Id'):
        waitforele = waitforElementPresentAction()
        element1 = waitforele.waitforElementPresentAction(webdriver, elementname, method)
        location1 = element1.location
        # 45 偏移量
        y = int(location1['y'])+60
        x = int(location1['x'])-60
        mymouse = PyMouse()
        mymouse.move(x, y)
        time.sleep(1)
        mymouse.click(x,y,1)
        time.sleep(1)

    def updatebook(self,webdriver,elementname='',method='Id'):
        waitforele = waitforElementPresentAction()
        element1 = waitforele.waitforElementPresentAction(webdriver, elementname, method)
        location1 = element1.location
        # 45 偏移量
        y = int(location1['y'])+60
        x = int(location1['x'])-90
        mymouse = PyMouse()
        mymouse.move(x, y)
        time.sleep(1)
        mymouse.click(x,y,1)
        time.sleep(1)

    def refreshbook(self,webdriver,elementname='',method='Id'):
        waitforele = waitforElementPresentAction()
        element1 = waitforele.waitforElementPresentAction(webdriver, elementname, method)
        location1 = element1.location
        # 45 偏移量
        y = int(location1['y'])+60
        x = int(location1['x'])-120
        mymouse = PyMouse()
        mymouse.move(x, y)
        time.sleep(1)
        mymouse.click(x,y,1)
        time.sleep(1)

    def gettext(self,webdriver,elementname='',method='Id'):
        waitforele = waitforElementPresentAction()
        element1 = waitforele.waitforElementPresentAction(webdriver, elementname, method)
        text = element1.text
        return text

    def sendkeys(self,booknum,webdriver,elementname='',method='Id'):
        waitforele = waitforElementPresentAction()
        element1 = waitforele.waitforElementPresentAction(webdriver, elementname, method)
        time.sleep(1)
        element1.send_keys(booknum)

class waitforElementPresentAction():
    def __init__(self):
        self.localreadconfig = rConfig.ReadConfig()
        self.timeout = self.localreadconfig.get_http("timeout")

    def waitforElementPresentAction(self, webdriver, elementname='', method='Id'):
        'method value:Id,Name,Class,xpath;webdriver value Firefox,Ie,takes a WebDriver instance and timeout in seconds'
        element1 = None
        end_time = time.time() + int(self.timeout)
        while True:
            try:
                if method == 'Id':
                    element1 = webdriver.find_element_by_id(elementname)
                elif method == 'Name':
                    element1 = webdriver.find_element_by_name(elementname)
                elif method == 'Class':
                    element1 = webdriver.find_element_by_class_name(elementname)
                elif method == 'Xpath':
                    element1 = webdriver.find_element_by_xpath(elementname)
                if element1:
                    return element1
            except Exception:
                pass
            if time.time() > end_time:
                assert False, 'NoSuchElementException ' + elementname + ' with the method ' + method
