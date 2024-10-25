from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@allure.title("Practice with Selenium Python")
@allure.description("Interacting with various fields with selenium python")
@pytest.mark.task24oct
def test_verify_selenium_practice():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://awesomeqa.com/practice.html")
        driver.find_element(by=By.XPATH, value="//input[@type='radio' and @value='Female']").click()
        driver.find_element(by=By.XPATH, value="//input[@type='checkbox' and @value='Automation Tester']").click()
        driver.find_element(by=By.XPATH, value="//input[@type='radio' and @value='3']").click()
    except NoSuchElementException as Nse:
        print("", Nse)
