from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Constructor


class TestConstructor:

    def test_menu_navigation_fillings(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        time.sleep(1)
        driver.find_element(*Constructor.locator_fillings()).click()
        time.sleep(1)
        element = Constructor.locator_meteorite()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(element))
        driver.quit()

    def test_menu_navigation_sauces(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        time.sleep(1)
        driver.find_element(*Constructor.locator_sauces()).click()
        time.sleep(1)
        element = Constructor.locator_spicy()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(element))
        driver.quit()

    def test_menu_navigation_buns(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        time.sleep(1)
        driver.find_element(*Constructor.locator_sauces()).click()
        time.sleep(1)
        driver.find_element(*Constructor.locator_buns()).click()
        time.sleep(1)
        element = Constructor.locator_bun_flu()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(element))
        driver.quit()
