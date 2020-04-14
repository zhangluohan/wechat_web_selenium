from selenium.webdriver.common.by import By

from po.page.basePage import BasePage


class SearchResultPage(BasePage):
    _edit_button = (By.CSS_SELECTOR, '.js_edit')
    _name = (By.CSS_SELECTOR, '#username')
    _save = (By.CSS_SELECTOR, 'a.qui_btn.ww_btn.ww_btn_Blue.js_save')
    _save_successful = (By.CSS_SELECTOR, '.ww_tip.success')

    def edit_person(self, name_edit):
        '''
        *是因为find_element需要两个参数，而属性字段是元组，是一个字段，所以用*将元组的字段拆分成两个字段
        可改成自己的find方法
        self.driver.find_element(*self._edit_button).click()
        self.driver.find_element(*self._name).send_keys(name_edit)
        self.driver.find_element(*self._save).click()
        '''
        self.find(self._edit_button).click()
        self.find(self._name).send_keys(name_edit)
        self.find(self._save).click()

        return self

    def edit_result_successful(self):
        return self.find(self._save_successful).text


