from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
import urls


class TestConstructor:

    def test_menu_navigation_fillings(self, browser):
        browser.get(urls.MAIN_URL)
        browser.find_element(*locators.BUTT_FILL).click()
        element = locators.FILL_METEOR
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))

    def test_menu_navigation_sauces(self, browser):
        browser.get(urls.MAIN_URL)
        browser.find_element(*locators.BUTT_SAU).click()
        element = locators.SAU_SPICY
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))

    def test_menu_navigation_buns(self, browser):
        browser.get(urls.MAIN_URL)
        browser.find_element(*locators.BUTT_FILL).click()
        browser.find_element(*locators.BUTT_BUNS).click()
        element = locators.BUN_FLU
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))

