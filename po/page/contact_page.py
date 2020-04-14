from selenium.webdriver.common.by import By

from po.page.basePage import BasePage
from po.page.search_result_page import SearchResultPage


class ContactPage(BasePage):# 继承父类driver，也可以自己用init方法重构

    _add_button = (By.CSS_SELECTOR, '.js_add_sub_party')
    _cancel = (By.CSS_SELECTOR, '#__dialog__MNDialog__ > div > div.qui_dialog_foot.ww_dialog_foot > a:nth-child(2)')
    _search_text = (By.CSS_SELECTOR, '#memberSearchInput')

    def add_person(self):
        self.find(self._add_button).click()
        self.find(self._cancel).click()
        return self

    def delete_person(self):
        return self

    def search_person(self, username):
        self.find(self._search_text).clear()
        self.find(self._search_text).send_keys(username)
        return SearchResultPage()
