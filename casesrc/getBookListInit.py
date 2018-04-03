# -*- coding: utf-8 -*-
from SetupIE import SetupIE
from common.elementActionUtil import ElementAction
import time
import random

class BookListInit():
    def __init__(self):
        pass

    def book_list_click(self):
        getIE = SetupIE()
        driver = getIE.setup_IE()
        #图书管理xpath
        bookmanagexpath = ".//*[@id='treeview-1015-record-book_manage']/td/div/span[text()='图书管理']"
        method = 'Xpath'
        elementaction = ElementAction()
        elementaction.singleclickpos(driver,bookmanagexpath, method)
        return driver

"""
if __name__ == "__main__":
    booklistinit = BookListInit()
    driver = booklistinit.book_list_click()
    time.sleep(3)
#    driver.quit()
    addpath = ".//*[@id='button-1045-btnInnerEl']"
    method = 'Xpath'
    elementaction = ElementAction()
    elementaction.singleclickpos(driver, addpath, method)
    time.sleep(2)

    for handle in driver.window_handles:#方法二，始终获得当前最后的窗口
        driver.switch_to_window(handle)
    idelement = driver.find_element_by_xpath(".//*[@id='numberfield-1053-inputEl']")
    print idelement
    time.sleep(1)
    idelement.click()
    time.sleep(1)
    a = random.uniform(10, 100)
    idelement.send_keys(int(a))
"""

"""
    element1 = \
            driver.find_element_by_xpath(".//*[@id='gridview-1043-record-1']/td[1]/div")
    print element1
    text = element1.text
    print text
"""


