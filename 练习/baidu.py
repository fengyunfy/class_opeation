from selenium import webdriver
from time import sleep
driver = webdriver.Edge()
driver.get("https://www.baidu.com/")
sleep(3)
driver.find_element(by.id("kw")).send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(3)
driver.quit()