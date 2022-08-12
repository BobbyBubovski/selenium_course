from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__name__))

file_path = os.path.join(current_dir, 'API.txt')
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME,"firstname")
    first_name.send_keys("Bobby")

    first_name = browser.find_element(By.NAME, "lastname")
    first_name.send_keys("Bubovski")

    first_name = browser.find_element(By.NAME, "email")
    first_name.send_keys("booboo@gmail.com")

    choose_file = browser.find_element(By.NAME,"file")
    choose_file.send_keys(file_path)



    button = browser.find_element(By.TAG_NAME,"button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()


finally:
    time.sleep(10)
    browser.quit()