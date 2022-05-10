from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element_by_id("num1").text)
    y = int(browser.find_element_by_id("num2").text)

    sum = str(x + y)

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value='"+sum+"']").click()

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()