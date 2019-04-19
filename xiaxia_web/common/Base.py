import time
from selenium import  webdriver

#注释的快捷键，ctrl+/
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class Base():
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
        self.timeout = 10
        self.t = 0.5

    def findElement(self,locator):
        eles = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_element(*locator))
        return eles

    def findElements(self,locator):
        eles = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_elements(*locator))
        return eles


    def sendtext(self,locator,name):
        ele = self.findElement(locator)
        ele.send_keys(name)

    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()

    def findNewEle(self,locator):
        #定位元素返回元素对象，未定位到，返回timeout
        ele =  WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
        return ele

    def istitle(self,title):
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
        return  result

    def iscontainstitle(self,title):
        result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
        return  result

    def isTextinEle(self,locator,textname):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator,textname))
            return result
        except:
            return False


    def isAlert(self):
        try:
            result_alert = WebDriverWait(self.driver,self.timeout,self.t).until(EC.alert_is_present())
            result_alert.accept()
            return result_alert
        except:
            return False



#鼠标悬停事件
    def move_to_element(self,locator):
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()


    def js_focus_element(self,locator):
        '''聚焦元素'''
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0, 0)"
        driver.execute_script(js)

    def js_sroll_end(self,x=0):
        '''滚动到底部,若为横向滚动改变x的值'''
        js = "window.scrollTo(%s,document.body.scrollHeight)"%x




if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://10.155.20.210/pms/index.php?m=user&f=login")

    op = Base(driver)

    la =(By.XPATH,"//*[@id='account']")

    la1 = (By.CSS_SELECTOR,"#account")
    la2 = (By.CSS_SELECTOR,"[name='password']")
    la3=(By.XPATH,".//*[@id='submit']")

    op.sendtext(la1,"zhuhongxia")
    op.sendtext(la2,"zhuhongxia1")

    time.sleep(2)
    # r = op.findElement(la1).text
    # print(r)
    op.click(la3)

    result = op.isAlert()
    print(result)

    if result:
        result.accept()

    # la1 = (By.XPATH,".//*[@id='login-form']/form/table/tbody/tr[4]/td/a")
    #
    # op.sendtext(la,"zhuhongxia")
    #
    # r1= op.istitle("用户登录 - 禅道")
    # print(r1)
    #
    # r2 = op.iscontainstitle("用户")
    # print(r2)
    #
    # r3 = op.isTextinEle(la1,"忘记密码")
    # print(r3)