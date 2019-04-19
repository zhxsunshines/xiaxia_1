import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from common.Base import Base


class addBug(Base):
    #登录
    la1 = (By.CSS_SELECTOR,"#account")
    la2 = (By.CSS_SELECTOR,"[name='password']")
    la3=(By.XPATH,".//*[@id='submit']")

    #添加bug
    cilcktest = (By.XPATH,".//*[@id='mainmenu']/ul/li[4]/a")
    clickbug = (By.XPATH,".//*[@id='modulemenu']/ul/li[2]/a")
    addp=(By.XPATH ,".//*[@id='featurebar']/div[1]/div[2]/a[2]")
    trunk = (By.XPATH , ".//*[@id='openedBuild_chosen']/ul")
    choosetrunk = (By.XPATH,".//*[@id='openedBuild_chosen']/div/ul/li")
    zhipai = (By.XPATH,".//*[@id='assignedTo_chosen']/a")
    # zhipai1 = (By.XPATH,".//*[@id='assignedTo_chosen']/div/ul/li[1]")


    #bug内容
    bugtitle = (By.ID,"title")
    bodycotext = (By.CLASS_NAME,"article-content")
    submit = (By.CSS_SELECTOR,"#submit")

    titlename = (By.XPATH,".//*[@id='bugList']/tbody/tr[1]/td[4]/a")



    def loginZentao(self,name = "zhuhongxia",pwd="zhuhongxia"):
        self.driver.get("http://10.155.20.210/pms/index.php?m=user&f=login")
        self.sendtext(self.la1,name)
        self.sendtext(self.la2,pwd)
        self.click(self.la3)

    def addtest(self,_title):
        self.click(self.cilcktest)
        self.click(self.clickbug)
        self.click(self.addp)
        self.click(self.trunk)
        self.click(self.choosetrunk)
        self.click(self.zhipai)
        # self.click(self.zhipai1)

    #遍历li下拉列表
        # pailist = self.driver.find_elements_by_xpath(".//*[@id='assignedTo_chosen']/div/ul/li")
        time.sleep(2)
        pailist = self.findElements((By.XPATH,".//*[@id='assignedTo_chosen']/div/ul/li"))

        for i in pailist:
            if "郭晓" in  i.text:
                i.click()
                break

        self.sendtext(self.bugtitle, _title)
        #切换至相应的iframe
        frame = self.findElement(("class name","ke-edit-iframe"))
        self.driver.switch_to.frame(frame)

        #body富文本不能clear
        self.sendtext(self.bodycotext,"测试内容")

        # a = "内容"
        # js = "document.getElementsByClassName(\"ke-edit-iframe\")[0].contentWindow.document.body.innerHTML=\"%s\"" % a
        # driver.execute_script(js)
        time.sleep(1)
        self.driver.switch_to.default_content()

        self.click(self.submit)

    def isaddSucess(self,_title):
        result  = self.isTextinEle(self.titlename,_title)
        return  result




if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://10.155.20.210/pms/index.php?m=user&f=login")

    a = addBug(driver)

    t = time.strftime("%Y_%m_%d_%H_%M_%S")
    title = "山桃街bug"+ t

    a.loginZentao()
    a.addtest(title)

    # result  = a.isaddSucess(title)
    # print(result)
