from selenium import webdriver
from selenium.webdriver.common.by import By
import time





link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input" )
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
    input3.send_keys("raduga@gmail.com")
    input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
    input4.send_keys("+380956783456")
    input5 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

