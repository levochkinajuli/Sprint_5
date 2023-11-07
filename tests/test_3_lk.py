from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
import urls
import data
import time


class TestLoginPage:

    def test_button_lk(self, browser):
        browser.get(urls.MAIN_URL)
        browser.find_element(*locators.BUTT_LK).click()
        browser.find_element(*locators.EMAIL).send_keys(data.EMAIL)
        browser.find_element(*locators.PASSWORD).send_keys(data.PASSWORD)
        browser.find_element(*locators.BUTT_ENTER).click()
        a = locators.BUTT_ORDER
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(a))
        assert browser.find_element(*locators.BUTT_ORDER).text == 'Оформить заказ'

    def test_from_lk_to_constructor(self, browser):
        browser.get(urls.MAIN_URL)
        browser.find_element(*locators.BUTT_LK).click()
        browser.find_element(*locators.EMAIL).send_keys(data.EMAIL)
        browser.find_element(*locators.PASSWORD).send_keys(data.PASSWORD)
        browser.find_element(*locators.BUTT_ENTER).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(locators.BUTT_LK))
        browser.find_element(*locators.BUTT_LK).click()
        browser.find_element(*locators.BUTT_CONS).click()
        assert browser.find_element(*locators.BUTT_ORDER).text == 'Оформить заказ'

    def test_logout_from_lk(self, browser):
        browser.get(urls.MAIN_URL)
        browser.find_element(*locators.BUTT_LK).click()
        browser.find_element(*locators.EMAIL).send_keys(data.EMAIL)
        browser.find_element(*locators.PASSWORD).send_keys(data.PASSWORD)
        browser.find_element(*locators.BUTT_ENTER).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(locators.BUTT_LK))
        browser.find_element(*locators.BUTT_LK).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(locators.BUTT_LOGOUT))
        browser.find_element(*locators.BUTT_LOGOUT).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(locators.BUTT_ENTER))
        assert 'login' in browser.current_url

    def test_from_lk_to_header_logo(self, browser):
        browser.get(urls.MAIN_URL)
        browser.find_element(*locators.BUTT_LK).click()
        browser.find_element(*locators.EMAIL).send_keys(data.EMAIL)
        browser.find_element(*locators.PASSWORD).send_keys(data.PASSWORD)
        browser.find_element(*locators.BUTT_ENTER).click()
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(locators.BUTT_LK))
        browser.find_element(*locators.BUTT_LK).click()
        browser.find_element(*locators.BUTT_LOGO).click()
        assert browser.find_element(*locators.BUTT_ORDER).text == 'Оформить заказ'
