from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By
import logging


@allure.title("Task 2")
def test_verify_make_appointment():
    logger = logging.getLogger()
    logger.info("Test Execution Started.......................")
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.page_load_strategy = 'normal'
    options.unhandled_prompt_behavior = 'accept'
    driver = webdriver.Chrome(options=options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.find_element(By.ID, "btn-make-appointment").click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").submit()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    logger.info("Test Execution Ended.......................")
    driver.quit()
