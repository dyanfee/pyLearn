from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
path = "chromedriver.exe"
# path =
driver = webdriver.Chrome(executable_path=path)

url = "https://www.baidu.com"
driver.get(url)

text = driver.find_element_by_id("wrapper").text

# print(text)
# print(driver.title)

driver.save_screenshot('index.png')
# "kw" 是百度输入框
driver.find_element_by_id("kw").send_keys(u'啦啦啦')

# "su" 是百度搜索按钮
driver.find_element_by_id("su").click()

time.sleep(5)

# 获取当前界面cookie
print(driver.get_cookies())

#  模拟输入两个按键  "Ctrl + a"
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "a")
#  " Ctrl + x"
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "x")

driver.find_element_by_id("kw").send_keys(u"大熊猫")
driver.find_element_by_id("su").send_keys(Keys.RETURN)

time.sleep(5)
driver.save_screenshot("panda.png")

driver.find_element_by_id("kw").clear()
driver.save_screenshot("quit.png")

driver.quit()
