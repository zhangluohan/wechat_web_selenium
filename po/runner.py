import pytest

from po.initbility.wechat_driver import WeChatDriver


if __name__ == '__main__':
    WeChatDriver.we_chat_driver()

    pytest.main(['testcase/test_pocase.py'])

    WeChatDriver.we_chat_driver_quit()
