# -*- coding: utf-8 -*-
from getBookListInit import BookListInit
import time
import random
from common.elementActionUtil import ElementAction
from selenium.webdriver.common.keys import Keys

class AddBook():
    def __init__(self):
        pass

    def add_book(self):
        booklistinit = BookListInit()
        driver = booklistinit.book_list_click()
        time.sleep(1)
        #    driver.quit()
        addpath = ".//*[@id='button-1045-btnInnerEl']"
        method = 'Xpath'
        elementaction = ElementAction()
        elementaction.singleclickpos(driver, addpath, method)
        time.sleep(1)

        #切换窗口
        for handle in driver.window_handles:  # 始终获得当前最后的窗口
            driver.switch_to_window(handle)
        #输入ID
        idxpath = ".//*[@id='numberfield-1053-inputEl']"
        method = 'Xpath'
#       时间关系，暂时用随机数代替
        a = int(random.uniform(10, 100))
        elementaction.sendkeys(a, driver, idxpath, method)
        #输入name
        namexpath = ".//*[@id='textfield-1054-inputEl']"
        elementaction.sendkeys(a, driver, namexpath, method)
        #输入author
        authorxpath = ".//*[@id='textfield-1055-inputEl']"
        elementaction.sendkeys(a, driver, authorxpath, method)
        #输入year
        yearxpath = ".//*[@id='numberfield-1056-inputEl']"
        elementaction.sendkeys(a, driver, yearxpath, method)
        #输入digest
        digestxpath = ".//*[@id='textarea-1057-inputEl']"
        elementaction.sendkeys(a, driver, digestxpath, method)
        #提交
        summitxpath = ".//*[@id='button-1059']"
        elementaction.sendkeys(Keys.ENTER, driver, summitxpath, method)
        #点击ok
        for handle in driver.window_handles:  # 始终获得当前最后的窗口
            driver.switch_to_window(handle)
        okxpath = ".//*[@id='button-1005-btnIconEl']"
        elementaction.sendkeys(Keys.ENTER, driver, okxpath, method)
        #关闭窗口
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    addbook =AddBook()
    addbook.add_book()

