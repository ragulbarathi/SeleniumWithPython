from selenium import webdriver
import allure
import pytest


def test_verify_title():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    assert driver.title == "CURA Healthcare Service"
