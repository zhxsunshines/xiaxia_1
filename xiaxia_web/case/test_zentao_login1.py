import  unittest
import  time
from selenium import webdriver

from common.loginzentao import loginzentao


class testLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver =  webdriver.Chrome() #打开浏览器
        cls.zentao = loginzentao(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()      #退出浏览器, 关闭浏览器进程


    #每个用例执行之前执行
    def setUp(self):
        self.driver.get("http://10.155.20.210/pms/index.php?m=user&f=login")

    def tearDown(self):
        self.zentao.is_alert_exist()        #点击判断是否有alert弹出框
        self.driver.delete_all_cookies()    #清空浏览器缓存
        self.driver.refresh()

    #输入正确的用户名、密码，判断是否登录成功
    def test1(self):
        '''输入正确的用户名、密码'''
        time.sleep(2)
        #输入用户名、密码，点击登录
        self.zentao.login("zhuhongxia","zhuhongxia")

        t = self.zentao.loginnameisTure()
        print("获取的结果：%s"%t)

        self.assertTrue(t == "朱红霞")

    #输入错误的用户名、密码
    def test2(self):
        '''输入错误的用户名、密码'''
        time.sleep(2)
        self.zentao.login("zhuhongxia","zhuhongxia1")
        t = self.zentao.loginnameisTure()
        print("登录失败，获取的结果：%s"%t)

        # 判断获取的用户名是否为空
        self.assertTrue(t == "")


if __name__ == '__main__':
    unittest.main()

