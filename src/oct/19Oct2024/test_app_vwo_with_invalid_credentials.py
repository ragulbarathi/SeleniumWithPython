from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Verify app.vwo login page with invalid credentials")
@allure.description("Verify that the user is able to see an error message on login with invalid credentials.")
@pytest.mark.task19oct
def test_app_vwo_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.find_element(by=By.ID, value="login-username").send_keys("ragul")
    driver.find_element(by=By.ID, value="login-password").send_keys("ravibarathi")
    driver.find_element(by=By.XPATH, value="//button[@id='js-login-btn']").click()
    try:
        element = By.ID, "js-notification-box-msg"
        WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(locator=element,
                                                                        text_="Your email, password, IP address or location did not match"))
    finally:
        driver.quit()
