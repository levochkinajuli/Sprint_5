from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators import ConstructorLocators
from conftest import browser


class TestConstructor:

    def test_menu_navigation_fillings(self, browser):
        browser.get(Urls.MAIN_URL)
        browser.find_element(*ConstructorLocators.BUTT_FILL).click()
        element = ConstructorLocators.FILL_METEOR
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))
        assert 'Говяжий' in browser.find_element(*ConstructorLocators.FILL_METEOR).text

    def test_menu_navigation_sauces(self, browser):
        browser.get(Urls.MAIN_URL)
        browser.find_element(*ConstructorLocators.BUTT_SAU).click()
        element = ConstructorLocators.SAU_SPICY
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))
        assert 'Соус Spicy-X' in browser.find_element(*ConstructorLocators.SAU_SPICY).text

    def test_menu_navigation_buns(self, browser):
        browser.get(Urls.MAIN_URL)
        browser.find_element(*ConstructorLocators.BUTT_FILL).click()
        browser.find_element(*ConstructorLocators.BUTT_BUNS).click()
        element = ConstructorLocators.BUN_FLU
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))
        assert 'Флюоресцентная булка R2-D3' in browser.find_element(*ConstructorLocators.BUN_FLU).text

