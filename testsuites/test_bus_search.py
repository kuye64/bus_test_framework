# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.bus_homepage import HomePage
from pageobjects.login_page import LoginPage
from selenium import webdriver

class BusSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        #cls.driver.quit()

    def test_bus_login(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
         """
        loginpage = LoginPage(self.driver)
        loginpage.type_search_user("13418683524")  # 调用页面对象中的方法
        time.sleep(2)
        loginpage.type_search_paswd("123456")  # 调用页面对象中的方法
        time.sleep(2)
        loginpage.click_button()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        loginpage.baedata()
        loginpage.switch()
        loginpage.get_windows_img()  # 调用基类截图方法


    def test_basedata_first(self): # 首页

        time.sleep(2)
        print("首页-调整滚动条查询数据成功")
        #     homepage = HomePage(self.driver)
        #     homepage.type_search('python')  # 调用页面对象中的方法
        #     homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        #     time.sleep(2)
        #     homepage.get_windows_img()  # 调用基类截图方法


# def test_baidu_search(self):
#     """
#     这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
#     :return:
#     """
#     homepage = HomePage(self.driver)
#     homepage.type_search('selenium')  # 调用页面对象中的方法
#     homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
#     time.sleep(2)
#     homepage.get_windows_img()  # 调用基类截图方法
#     try:
#         assert 'selenium' in homepage.get_page_title()  # 调用页 面对象继承基类中的获取页面标题方法
#         print('Test Pass.')
#     except Exception as e:
#         print('Test Fail.', format(e))
#
#
# def test_search2(self):
#     homepage = HomePage(self.driver)
#     homepage.type_search('python')  # 调用页面对象中的方法
#     homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
#     time.sleep(2)
#     homepage.get_windows_img()  # 调用基类截图方法


if __name__ == '__main__':
    unittest.main()
