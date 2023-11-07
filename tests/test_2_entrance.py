from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
import urls
import data


class TestLoginPage:

    def test_button_entrance(self, browser):
        browser.get(urls.MAIN_URL)
        browser.find_element(*locators.BUTT_ENTER_MAIN).click()
        element = locators.BUTT_ENTER
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))
        browser.find_element(*locators.EMAIL).send_keys(data.EMAIL)
        browser.find_element(*locators.PASSWORD).send_keys(data.PASSWORD)
        browser.find_element(*locators.BUTT_ENTER).click()
        assert 'site' in browser.current_url

    def test_button_lk(self, browser):
        browser.get(urls.MAIN_URL)
        browser.find_element(*locators.BUTT_LK).click()
        element = locators.BUTT_ENTER
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))
        browser.find_element(*locators.EMAIL).send_keys(data.EMAIL)
        browser.find_element(*locators.PASSWORD).send_keys(data.PASSWORD)
        browser.find_element(*locators.BUTT_ENTER).click()
        assert 'site' in browser.current_url

    def test_entrance_button_in_reg_form(self, browser):
        browser.get(urls.REG_URL)
        browser.find_element(*locators.BUTT_ALR_REG).click()
        element = locators.BUTT_ENTER
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))
        browser.find_element(*locators.EMAIL).send_keys(data.EMAIL)
        browser.find_element(*locators.PASSWORD).send_keys(data.PASSWORD)
        browser.find_element(*locators.BUTT_ENTER).click()
        assert 'site' in browser.current_url

    def test_button_forgot_password(self, browser):
        browser.get(urls.LK_URL)
        browser.find_element(*locators.BUTT_REST_PASS).click()
        element = locators.BUTT_ALR_REG
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))
        browser.find_element(*locators.BUTT_ALR_REG).click()
        browser.find_element(*locators.EMAIL).send_keys(data.EMAIL)
        browser.find_element(*locators.PASSWORD).send_keys(data.PASSWORD)
        browser.find_element(*locators.BUTT_ENTER).click()
        assert 'site' in browser.current_url


