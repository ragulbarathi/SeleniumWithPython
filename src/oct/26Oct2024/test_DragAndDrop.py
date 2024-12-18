import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


@allure.title("Actions task ")
@allure.description("Drag and Drop")
def test_drgdnddrp():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    drgele = driver.find_element(by=By.XPATH, value="//div[@id='draggable']")
    drpele = driver.find_element(by=By.XPATH, value="//div[@id='droppable']")

    actions = ActionChains(driver=driver)
    actions.drag_and_drop(drgele, drpele).perform()
