from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://github.com/login')

elem = driver.find_element_by_id('login_field')
time.sleep(2)
elem.clear()
elem.send_keys(username)  # Enter your GitHub username as string

elem = driver.find_element_by_id('password')
time.sleep(2)
elem.clear()
elem.send_keys(password)  # Enter your GitHub password as string

elem = driver.find_element(By.XPATH, '//*[@id="login"]/form/div[3]/input[8]')
time.sleep(2)
elem.click()

# Uncomment the line below and change it to use your username and repository name such as :
# driver.get('https://github.com/Your Username/Your Existing Github Repo Name/new/master?readme=1')
# ex: driver.get('https://github.com/JerinFrancisA/GitHub-Automation/new/master?readme=1')

elem = driver.find_element(By.XPATH, '//*[@id="js-repo-pjax-container"]/div[2]/div/div/form[2]/div[1]/span/input')
time.sleep(2)
elem.clear()
elem.send_keys(str(datetime.today())+'.md')
time.sleep(4)

elem = driver.find_element(By.ID, 'submit-file')
time.sleep(2)
elem.click()
