import time
import unittest

from selenium import webdriver

from pages.addBug import addBug
from pages.login_page import Loginpage


class test_add_bug(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

        cls.login = Loginpage(cls.driver)

        cls.a = addBug(cls.driver)
        cls.login.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def setUp(self):
        self.driver.get(".//*[@id='mainmenu']/ul/li[1]/a/span")


    def test_addbug_1(self):
        t = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "山桃街bug" + t

        self.a.addtest(title)
        result  = self.a.isaddSucess(title)
        print(result)

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
