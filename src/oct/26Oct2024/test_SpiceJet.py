import time

import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait


@allure.title("Spice Jet task ")
@allure.description("Find and Click Delhi")
def test_sample_booking():
    driver = webdriver.Chrome()
    driver.get("https://www.spicejet.com/")
    Fromele = driver.find_element(By.XPATH,
                                  value="//div[text()='From']")
    toele = driver.find_element(By.XPATH, value="//div[text()='To']")

    action = ActionChains(driver)
    action.click(Fromele).send_keys("Del").click(toele).send_keys("Maa").perform()
    time.sleep(5)
    dt = driver.find_element(By.XPATH, "//div[@data-testid='undefined-calendar-day-25']")
    WebDriverWait(driver, 10).until(
        Ec.visibility_of(dt))
    searchflightbtn = driver.find_element(By.XPATH, value="//div[@data-testid='home-page-flight-cta']")
    action.click(dt).click(searchflightbtn).perform()
