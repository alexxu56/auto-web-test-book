# -*- coding: utf-8 -*-
from getBookListInit import BookListInit
import time
import random
from common.elementActionUtil import ElementAction
from selenium.webdriver.common.keys import Keys

class RefreshBook():
    def __init__(self):
        pass

    def Refresh_book(self):
        #打开IE窗口、URL
        booklistinit = BookListInit()
        driver = booklistinit.book_list_click()
        time.sleep(1)

        method = 'Xpath'
        elementaction = ElementAction()
        #点击刷新按钮
        time.sleep(1)
        deletepath = ".//*[@id='button-1048-btnInnerEl']"
        elementaction.refreshbook(driver, deletepath, method)

if __name__ == "__main__":
    refreshbook =RefreshBook()
    refreshbook.Refresh_book()