import logging

from po.initbility.wechat_driver import WeChatDriver


class BasePage:

    def __init__(self):

        self.driver = WeChatDriver().driver

    @staticmethod
    def log():
        logging.basicConfig(level=logging.INFO)

    def find(self, locator, value=None):
        if value==None:
            return self.driver.find_element(*locator)
        else:
            return self.driver.find_element(*locator, value)
