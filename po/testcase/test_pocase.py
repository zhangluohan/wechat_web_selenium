import logging
from time import sleep

from po.page.contact_page import ContactPage
from po.page.search_result_page import SearchResultPage


class TestContact:

    contact_page = ContactPage()
    s_r_page = SearchResultPage()
    '''
    def test_add_person(self):
        self.contact_page.add_person()
        # assert

    def test_delete_person(self):
        # add_person() return self, 所以可以链式调用
        self.contact_page.add_person().delete_person()

    def test_search_person(self):
        self.contact_page.search_person("wang")
    '''

    def test_edit_person(self):
        self.contact_page.search_person("wang").edit_person("00001")  # 动态加时间戳："001 %s" % str(time())

        assert self.s_r_page.edit_result_successful() == "保存成功"
