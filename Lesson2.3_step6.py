from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input.send_keys(y)

    buttonSubmit = browser.find_element(By.CLASS_NAME, "btn-primary")
    buttonSubmit.click()


finally:
    time.sleep(10)
    browser.quit()
