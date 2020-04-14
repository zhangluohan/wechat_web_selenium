from selenium import webdriver


class WeChatDriver:

    driver = ''

    @classmethod
    def we_chat_driver(cls):
        # 也可以写成__init__方法，runner只要初始化此类就行

        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = "127.0.0.1:9222"
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cls.driver.implicitly_wait(5)

    @classmethod
    def we_chat_driver_quit(cls):
        cls.driver.quit()
