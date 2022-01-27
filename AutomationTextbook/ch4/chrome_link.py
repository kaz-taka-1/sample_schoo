from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://uta.pw/sakusibbs/')
link = driver.find_element_by_link_text('名作アーカイブ')
link.click()

time.sleep(30)
driver.close()