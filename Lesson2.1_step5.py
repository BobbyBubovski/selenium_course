from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"


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

    """"Проверка значения атрибутов с помощью метода get.attribute"""
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not  None, "People radio is not selected by default"
    """Способ проверки сравниванием строк"""
    #assert people_checked == "true", "People radio is not selected by default"

    robot_radio = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    robot_radio.click()

    submit_button = browser.find_element(By.XPATH,"/html/body/div/form/button")
    submit_button.click()




finally:
    time.sleep(10)
    browser.quit