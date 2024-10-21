from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By


@allure.title("Verify Register account page in open cart module")
@allure.description("Verify that the user is able to create an account for the open cart module.")
@pytest.mark.task19oct
def test_verify_register_account():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.page_load_strategy = 'normal'
    options.unhandled_prompt_behavior = 'accept'
    driver = webdriver.Chrome(options=options)
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    driver.find_element(by=By.ID, value="input-firstname").send_keys("ragul")
    driver.find_element(by=By.ID, value="input-lastname").send_keys("ravibarathi1234")
    driver.find_element(by=By.ID, value="input-email").send_keys("ragulravibarathi2@gmail.com")
    driver.find_element(by=By.ID, value="input-telephone").send_keys("04132964834")
    driver.find_element(by=By.ID, value="input-password").send_keys("Passwd@opencart")
    driver.find_element(by=By.ID, value="input-confirm").send_keys("Passwd@opencart")
    driver.find_element(by=By.XPATH, value="//input[@name='newsletter'][@value=0]").click()
    driver.find_element(by=By.XPATH, value="//input[@type='checkbox'][@value=1]").click()
    driver.find_element(by=By.XPATH, value="//input[@type='submit']").submit()
    assert driver.find_element(by=By.TAG_NAME, value="h1").text == "Your Account Has Been Created!"
