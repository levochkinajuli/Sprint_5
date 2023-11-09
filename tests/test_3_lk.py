from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from data import Entrance
from locators import MainPageLocators, LoginPageLocators
from conftest import browser

class TestLoginPage:

    def test_button_lk(self, browser):
        browser.get(Urls.MAIN_URL)
        browser.find_element(*MainPageLocators.BUTT_LK).click()
        browser.find_element(*LoginPageLocators.EMAIL).send_keys(Entrance.EMAIL)
        browser.find_element(*LoginPageLocators.PASSWORD).send_keys(Entrance.PASSWORD)
        browser.find_element(*LoginPageLocators.BUTT_ENTER).click()
        a = MainPageLocators.BUTT_ORDER
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(a))
        assert browser.find_element(*MainPageLocators.BUTT_ORDER).text == 'Оформить заказ'

    def test_from_lk_to_constructor(self, browser):
        browser.get(Urls.MAIN_URL)
        browser.find_element(*MainPageLocators.BUTT_LK).click()
        browser.find_element(*LoginPageLocators.EMAIL).send_keys(Entrance.EMAIL)
        browser.find_element(*LoginPageLocators.PASSWORD).send_keys(Entrance.PASSWORD)
        browser.find_element(*LoginPageLocators.BUTT_ENTER).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(MainPageLocators.BUTT_LK))
        browser.find_element(*MainPageLocators.BUTT_LK).click()
        browser.find_element(*MainPageLocators.BUTT_CONS).click()
        assert browser.find_element(*MainPageLocators.BUTT_ORDER).text == 'Оформить заказ'

    def test_logout_from_lk(self, browser):
        browser.get(Urls.MAIN_URL)
        browser.find_element(*MainPageLocators.BUTT_LK).click()
        browser.find_element(*LoginPageLocators.EMAIL).send_keys(Entrance.EMAIL)
        browser.find_element(*LoginPageLocators.PASSWORD).send_keys(Entrance.PASSWORD)
        browser.find_element(*LoginPageLocators.BUTT_ENTER).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(MainPageLocators.BUTT_LK))
        browser.find_element(*MainPageLocators.BUTT_LK).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(LoginPageLocators.BUTT_LOGOUT))
        browser.find_element(*LoginPageLocators.BUTT_LOGOUT).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(LoginPageLocators.BUTT_ENTER))
        assert 'login' in browser.current_url

    def test_from_lk_to_header_logo(self, browser):
        browser.get(Urls.MAIN_URL)
        browser.find_element(*MainPageLocators.BUTT_LK).click()
        browser.find_element(*LoginPageLocators.EMAIL).send_keys(Entrance.EMAIL)
        browser.find_element(*LoginPageLocators.PASSWORD).send_keys(Entrance.PASSWORD)
        browser.find_element(*LoginPageLocators.BUTT_ENTER).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(MainPageLocators.BUTT_LK))
        browser.find_element(*MainPageLocators.BUTT_LK).click()
        browser.find_element(*MainPageLocators.BUTT_LOGO).click()
        assert browser.find_element(*MainPageLocators.BUTT_ORDER).text == 'Оформить заказ'
