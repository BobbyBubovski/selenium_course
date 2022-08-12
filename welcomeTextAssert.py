from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    
    
    input1 = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    # вот тут валится второй тест, т.к. на второй станичке отсутствует поле для last name
    # No such element
    input2 = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    input2.send_keys("Ivan")
    input3 = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
    input3.send_keys("Ivan")
   

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()