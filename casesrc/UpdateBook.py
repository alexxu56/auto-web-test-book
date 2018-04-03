# -*- coding: utf-8 -*-
from getBookListInit import BookListInit
import time
import random
from common.elementActionUtil import ElementAction
from selenium.webdriver.common.keys import Keys

class UpdateBook():
    def __init__(self):
        pass

    def update_book(self):
        #打开IE窗口、URL
        booklistinit = BookListInit()
        driver = booklistinit.book_list_click()
        time.sleep(1)
        #选择一行修改
        linepath = ".//*[@id = 'gridview-1043-record-1']/td[1]/div"
        method = 'Xpath'
        elementaction = ElementAction()
        elementaction.selectbook(driver, linepath, method)

        #点击修改按钮
        time.sleep(1)
        deletepath = ".//*[@id='button-1047-btnInnerEl']"
        elementaction.updatebook(driver, deletepath, method)

        # 切换窗口
        for handle in driver.window_handles:  # 始终获得当前最后的窗口
            driver.switch_to_window(handle)
        # 输入ID
        method = 'Xpath'
        #       时间关系，暂时用随机数代替
        a = int(random.uniform(10, 100))
        # 输入name
        namexpath = ".//*[@id='textfield-1054-inputEl']"
        elementaction.sendkeys(a, driver, namexpath, method)
        # 输入author
        authorxpath = ".//*[@id='textfield-1055-inputEl']"
        elementaction.sendkeys(a, driver, authorxpath, method)
        # 输入year
        yearxpath = ".//*[@id='numberfield-1056-inputEl']"
        elementaction.sendkeys(a, driver, yearxpath, method)
        # 输入digest
        digestxpath = ".//*[@id='textarea-1057-inputEl']"
        elementaction.sendkeys(a, driver, digestxpath, method)
        # 提交
        summitxpath = ".//*[@id='button-1059']"
        elementaction.sendkeys(Keys.ENTER, driver, summitxpath, method)
        # 点击ok
        for handle in driver.window_handles:  # 始终获得当前最后的窗口
            driver.switch_to_window(handle)
        okxpath = ".//*[@id='button-1005-btnIconEl']"
        elementaction.sendkeys(Keys.ENTER, driver, okxpath, method)


if __name__ == "__main__":
    updatebook =UpdateBook()
    updatebook.update_book()

