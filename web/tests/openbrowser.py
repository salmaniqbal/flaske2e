import time
import os
from selenium import webdriver

driver_directory = os.getcwd()
driver = webdriver.Chrome(driver_directory + '/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.google.com/')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()