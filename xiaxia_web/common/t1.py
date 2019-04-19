from selenium import  webdriver
import time


driver = webdriver.Firefox()
driver.get("http://bj.ganji.com/")

#滚动到底部
time.sleep(2)
# js="var q=document.documentElement.scrollTop=100000 "
js="window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)

time.sleep(5)
#滚动到顶部
js="window.scrollTo(0, 0)"
driver.execute_script(js)

#滚动到元素出现的位置
ele = driver.find_element_by_link_text("新车")
driver.execute_script("arguments[0].scrollIntoView();",ele)



