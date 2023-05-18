import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


os.environ['PATH'] += r"E:\Scrappy\seleniumDriver"
driver = webdriver.Chrome()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.implicitly_wait(5) 
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

username.send_keys('Admin')
password.send_keys('admin123')

btn = driver.find_element(By.CLASS_NAME,'orangehrm-login-button')
btn.click()

time.sleep(30)

# basic
# driver.get('https://www.seleniumeasy.com/')
# driver.implicitly_wait(3) 
# my_element = driver.find_element(By.CLASS_NAME,'fa-link')
# my_element.click()

# explict wait
# WebDriverWait(driver,30).until(
#     EC.text_to_be_present_in_element(
#         (By.XPATH,'//h2/a'),
#         'Failed to launch chrome browser using selenium 4.8.2'
#     )
# )
