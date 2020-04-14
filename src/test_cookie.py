import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(level=logging.INFO)


class TestAddPerson:

    def test_cookie(self):

            '''
            通过cookie实现
            cookie:第一次访问网站的时候，浏览器记录set-cookie
            之后再访问时，会将此值以cookie头的形式，植入请求中
            另，当如登录操作时，会追加cookie
            建议：用谷歌隐身模式浏览网页验证
            登录前：
            set-cookie: wwrtx.i18n_lan=zh; Domain=.work.weixin.qq.com; Path=/; Expires=Tue, 12 May 2020 11:46:21 GMT
            set-cookie: wwrtx.ref=direct; Domain=.work.weixin.qq.com; Path=/; HttpOnly
            set-cookie: wwrtx.refid=35890628392781302; Domain=.work.weixin.qq.com; Path=/; HttpOnly
            登录后：
            set-cookie: wwrtx.i18n_lan=zh
            set-cookie: wwrtx.d2st=a8954710
            set-cookie: wwrtx.sid=sfDDZIp4QVKx7IaR7bkvUkfi5NEvBUV7yCQxcJuzCxmCt1JaDwvD8FaXicAR2QgO;
            set-cookie: wwrtx.ltype=1
            set-cookie: wxpay.corpid=1970325116123918
            set-cookie: wxpay.vid=1688853788538317
            set-cookie: wwrtx.vst=puSBQWeE-bVhnRaR2ARqhlHBSaEyeVHjqYoP3IFB_79kriBSVms76RjIr-DVit74swhVXcUNsk3kRLGKCI9jQzxcEAgdSsMDvO_rblTrXyLwRiYw89oUBXaEVmYq0WvUdWFFx4uJu1RTu-aTIAf4jB_SkfnfBC1og_Xr9nrm8r4_4eojq-tlLma3h801hK52UPt2HflWNniM0GhglHW1T6vQiLUWJtRRoW11lXD0LkrWm_r73cmAaYyDBbHY4rNMwqFvthiCCsHj9MawJuDwdg
            set-cookie: wwrtx.logined=true
            '''

            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            url = "https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome"
            self.driver.get(url)

            # 加入cookie
            dict_cookie = {"wwrtx.d2st":"a6355336",
                           "wwrtx.sid":"sfDDZIp4QVKx7IaR7bkvUiypa6Yntp4hHd2ATxDeRN1oqRvX5gghMI5H0sWoOG6W",
                           "wwrtx.ltype":"1",
                           "wwrtx.corpid":"1970325116123918",
                           "wwrtx.vid":"1688853788538317",
                           "wwrtx.vst":"II1Hu8gAzGUwulqtZSSJE4Kh3BNCUsA0wGfp9d6z_g-RDeMoUVeRo7TqCxWw_3I7lN8hXRPBWEtL6CnhALKiqxa0CbbC8bNgjfVC_NEHrwp3hOvdV63o9qZkI4n2Jm_z_P9jURrTHcdXtWkM679IXYgHVQZSDAaIZMi7rxS5OWVoLEyZVOsefEx8CtZgN7ofev_esq6h8C5u7jjhOMiw5UuIXSUa-LZIcznZKudGfyhwl5PjVX_5JIG-Mz4amcTnuNktHe_6kNtyr38zivgvzQ"}
            for k, v in dict_cookie.items():
                self.driver.add_cookie({"name":k, "value":v})
            self.driver.get(url)

            '''
            chrome 开启 remote debug, 用的是chrome devtool protocal,
            可以开启远程调控端口，可以绕过很多功能，如登录
            具体方法：
            进入chrome的exe目录，执行chrome.exe --remote-debugging-port=9222
            输入127.0.0.1:9222
            执行代码
            保持页面不关闭
            
            chrome_options = webdriver.ChromeOptions()
            chrome_options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#manageTools")
            '''

            # 进入企业管理模块
            element_guanli = self.driver.find_element(By.CSS_SELECTOR, '#menu_manageTools')
            element_guanli.click()

            element_sucai = self.driver.find_element(By.XPATH, '//*[contains(text(),"素材库")]')
            logging.info(self.driver.window_handles)

            logging.info(element_sucai.text)
            element_sucai.click()

            element_pic = self.driver.find_element(By.CSS_SELECTOR, '.ww_icon_GrayPic')
            logging.info(element_pic.text)
            element_pic.click()

            add_pic_button = self.driver.find_element(By.CSS_SELECTOR, '.js_upload_file_selector')

            logging.info(add_pic_button.text)
            add_pic_button.click()

            upload_pic_icon = self.driver.find_element(By.CSS_SELECTOR, '#js_upload_input')
            '''
            浏览器操作不了的，用js注入的方式
            logging.info(upload_pic_icon.text)
            self.driver.execute_script("arguments[0].click()", upload_pic_icon)
            sleep(5)
    
            另外，遇到上传文件等问题，因已经超出selenium的控制范围
            所以，可以考虑接口上传的方式，或者直接绕过此操作，用强行加载的方式
            '''
            upload_pic_icon.send_keys("E:\wap\code\wechatWebSelenium\image\pic1.jpg")
            sleep(5)

            # 添加显示等待，等待图片加载完成后，点击完成按钮
            # 未加载完成时，有取消按钮，可利用page-source查找
            print(self.driver.page_source)

            WebDriverWait(self.driver, 5).until(
                expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, '.js_hongbao_confirm_cancel')))

            finish_button = self.driver.find_element(By.CSS_SELECTOR, '.js_next')
            self.driver.execute_script("arguments[0].click()", finish_button)

            self.driver.quit()
