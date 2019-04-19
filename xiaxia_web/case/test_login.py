from selenium import webdriver
import unittest
import ddt

from pages.login_page import Loginpage


testdatas = [
    {"user":"zhuhongxia","pwd":"zhuhongxia","expect":"朱红霞"},
    {"user":"zhuhongxia","pwd":"zhuhongxia1","expect":""},
    {"user":"zhuhongxia","pwd":"","expect":""}
            ]

login_url = "http://10.155.20.210/pms/index.php?m=user&f=login"

@ddt.ddt
class  Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(login_url)
        cls.login = Loginpage(cls.driver)


    def setUp(self):
        self.login.isAlert()
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.get(login_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def login_zen_tao(self,user,pwd,expect):
        self.login.inputUsername(user)
        self.login.inputPwd(pwd)
        self.login.click_login()

        result = self.login.loginnameisTure()
        print(result)
        self.assertTrue(result == expect)


    @ddt.data(*testdatas)
    def test_login_1(self,data):
        print("测试数据：%s" %data)
        self.login_zen_tao(data["user"],data["pwd"],data["expect"])
        print("-------pass---------")





if __name__ == '__main__':
    unittest.main()
