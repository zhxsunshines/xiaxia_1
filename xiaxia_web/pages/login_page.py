from selenium import  webdriver
from selenium.webdriver.common.by import By

from common.Base import Base

url = "http://10.155.20.210/pms/index.php?m=user&f=login"

class Loginpage(Base):
    #登录
    la1 = (By.CSS_SELECTOR,"#account")
    la2 = (By.CSS_SELECTOR,"[name='password']")
    la3=(By.XPATH,".//*[@id='submit']")

    loginName = (By.XPATH,".//*[@id='userMenu']/a")

    keeplogin_button=(By.XPATH,".//*[@id='keepLoginon']")

    backto=(By.XPATH,".//*[@id='mainmenu']/ul/li[1]/a/span")

    def inputUsername(self,uername):
        self.sendtext(self.la1,uername)

    def inputPwd(self,pwd):
        self.sendtext(self.la2, pwd)

    def click_login(self):
        self.click(self.la3)


    def keep_login_click(self):
        self.click(self.keeplogin_button)


    def login(self,username="zhuhongxia",pwd="zhuhongxia",keeplogin=False):
        self.driver.get(url)
        self.inputUsername(username)
        self.inputPwd(pwd)

        if keeplogin :
            self.keep_login_click()

        self.click_login()


    def loginnameisTure(self):
        try:
            loginname = self.findElement(self.loginName).text
            return loginname
        except:
            return ""




if __name__ == '__main__':
    driver = webdriver.Firefox()
    login = Loginpage(driver)

    login.login()
