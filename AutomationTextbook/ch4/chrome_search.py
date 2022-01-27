from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://google.com')

el = driver.find_element_by_name('q')
el.send_keys('Pythonの教科書')
el.submit()
time.sleep(30)
driver.close()