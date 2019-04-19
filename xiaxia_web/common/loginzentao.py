import  time

class  loginzentao(object):
    def __init__(self,driver):
        self.driver = driver

    def login(self,username,pwd):
        self.driver.find_element_by_xpath(".//*[@id='account']").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(pwd)
        self.driver.find_element_by_xpath(".//*[@id='submit']").submit()

#查看获取的用户名是否正确
    def loginnameisTure(self):
        try:
            loginname = self.driver.find_element_by_xpath(".//*[@id='userMenu']/a").text
            return loginname
        except:
            return ""

    def is_alert_exist(self):
        '''判断alert是不是'''
        try:
            time.sleep(2)
            alert = self.driver.switch_to_alert()
            text = alert.text
            alert.accept()   #点击确认按钮
            return  text
        except:
            return  ""