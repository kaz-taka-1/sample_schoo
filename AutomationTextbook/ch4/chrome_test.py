from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://python.org')
time.sleep(30)
driver.quit()