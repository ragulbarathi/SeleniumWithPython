import time

from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By


@allure.title("Verify list of macmini in ebay.com along with the prices")
@allure.description("Verify list of macmini in ebay.com along with the prices ")
@pytest.mark.task22oct
def test_verify_list_of_macmini_ebay():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
        searchbox = driver.find_element(by=By.XPATH, value="//input[@type='text'][@id='gh-ac']")
        searchbox.send_keys("Macmini")
        driver.find_element(by=By.XPATH, value="//input[@id='gh-btn']").click()
        time.sleep(3)
        listofMacmini = driver.find_elements(by=By.XPATH, value="//span[@role='heading']")
        listofMacminiprice = driver.find_elements(by=By.XPATH, value="//span[@class='s-item__price']")
        pricelist = []
        for i, element in enumerate(listofMacmini):
            pricelist.append(listofMacminiprice[i].text.strip("$,t,o,"))
            print(f"Title=  {element.text}           Price =  ${pricelist[i]}")
        x = []
        for j in pricelist:
            x = pricelist.append(float(j))
        print(f"Max={max(x)} and Min={min(x)}")
    except ValueError as E:
        print("Not converted into float", type(E))

    finally:
        driver.quit()
