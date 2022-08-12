

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x=x_element.text
    y=calc(x)

    input1 = browser.find_element(By.XPATH, "//*[@id='answer']")
    input1.send_keys(y)

    check_b1 = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
    check_b1.click()

    robot_radio = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
    robot_radio.click()

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


    #submit_button = browser.find_element(By.XPATH,"/html/body/div/form/button")
    #submit_button.click()



finally:
    time.sleep(10)
    browser.quit