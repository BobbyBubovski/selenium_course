from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math



link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    a_element = browser.find_element(By.CSS_SELECTOR, "#num1" )
    a = a_element.text
    x= int(a)



    b_element = browser.find_element(By.CSS_SELECTOR, "#num2" )
    b = b_element.text
    y = int(b)


    c = x+y



    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(c))  # ищем элемент с текстом "Python"

    submit = browser.find_element(By. TAG_NAME, "button" )
    submit.click()

    alert = browser.switch_to.alert
    alert.accept()




finally:
    time.sleep(5)
    browser.quit