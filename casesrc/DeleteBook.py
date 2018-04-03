# -*- coding: utf-8 -*-
from getBookListInit import BookListInit
import time
from common.elementActionUtil import ElementAction
from selenium.webdriver.common.keys import Keys

class DeleteBook():
    def __init__(self):
        pass

    def delete_book(self):
        booklistinit = BookListInit()
        driver = booklistinit.book_list_click()
        time.sleep(1)
        #    driver.quit()
        #选择一行删除
        linepath = ".//*[@id = 'gridview-1043-record-1']/td[1]/div"
        method = 'Xpath'
        elementaction = ElementAction()
        elementaction.selectbook(driver, linepath, method)
        #点击删除按钮
        time.sleep(1)
        deletepath = ".//*[@id='button-1046-btnInnerEl']"
        elementaction.actionbook(driver, deletepath, method)
        #确认按钮
        time.sleep(1)
        for handle in driver.window_handles:  # 始终获得当前最后的窗口
            driver.switch_to_window(handle)
        yespath= ".//*[@id='button-1006-btnIconEl']"
        elementaction.sendkeys(Keys.ENTER, driver, yespath, method)
        #确认删除结果
        time.sleep(2)
        for handle in driver.window_handles:  # 始终获得当前最后的窗口
            driver.switch_to_window(handle)
        successpath= ".//*[@id='button-1005-btnIconEl']"
        elementaction.sendkeys(Keys.ENTER, driver, successpath, method)

        #关闭窗口
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    deletebook =DeleteBook()
    deletebook.delete_book()