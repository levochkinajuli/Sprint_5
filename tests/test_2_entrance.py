from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from data import Entrance
from locators import MainPageLocators, LoginPageLocators
from conftest import browser

class TestLoginPage:

    def test_button_entrance(self, browser):
        browser.get(Urls.MAIN_URL)
        browser.find_element(*MainPageLocators.BUTT_ENTER_MAIN).click()
        element = LoginPageLocators.BUTT_ENTER
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))
        browser.find_element(*LoginPageLocators.EMAIL).send_keys(Entrance.EMAIL)
        browser.find_element(*LoginPageLocators.PASSWORD).send_keys(Entrance.PASSWORD)
        browser.find_element(*LoginPageLocators.BUTT_ENTER).click()
        assert 'site' in browser.current_url

    def test_button_lk(self, browser):
        browser.get(Urls.MAIN_URL)
        browser.find_element(*MainPageLocators.BUTT_LK).click()
        element = LoginPageLocators.BUTT_ENTER
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))
        browser.find_element(*LoginPageLocators.EMAIL).send_keys(Entrance.EMAIL)
        browser.find_element(*LoginPageLocators.PASSWORD).send_keys(Entrance.PASSWORD)
        browser.find_element(*LoginPageLocators.BUTT_ENTER).click()
        assert 'site' in browser.current_url

    def test_entrance_button_in_reg_form(self, browser):
        browser.get(Urls.REG_URL)
        browser.find_element(*LoginPageLocators.BUTT_ALR_REG).click()
        element = LoginPageLocators.BUTT_ENTER
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))
        browser.find_element(*LoginPageLocators.EMAIL).send_keys(Entrance.EMAIL)
        browser.find_element(*LoginPageLocators.PASSWORD).send_keys(Entrance.PASSWORD)
        browser.find_element(*LoginPageLocators.BUTT_ENTER).click()
        assert 'site' in browser.current_url

    def test_button_forgot_password(self, browser):
        browser.get(Urls.LK_URL)
        browser.find_element(*LoginPageLocators.BUTT_REST_PASS).click()
        element = LoginPageLocators.BUTT_ALR_REG
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))
        browser.find_element(*LoginPageLocators.BUTT_ALR_REG).click()
        browser.find_element(*LoginPageLocators.EMAIL).send_keys(Entrance.EMAIL)
        browser.find_element(*LoginPageLocators.PASSWORD).send_keys(Entrance.PASSWORD)
        browser.find_element(*LoginPageLocators.BUTT_ENTER).click()
        assert 'site' in browser.current_url


