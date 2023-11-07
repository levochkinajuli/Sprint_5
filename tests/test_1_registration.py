from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators
import urls
import data


class TestRegistrationPage:

    def test_registration_correct(self, browser):
        browser.get(urls.REG_URL)
        browser.find_element(*locators.NAME_REG).send_keys(data.NAME)
        browser.find_element(*locators.EMAIL_REG).send_keys(data.EMAIL_FOR_REG)
        browser.find_element(*locators.PASSWORD_REG).send_keys(data.PASSWORD)
        browser.find_element(*locators.REG_BUTT).click()
        element = locators.BUTT_ENTER
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))
        assert browser.find_element(*locators.BUTT_ENTER).text == 'Войти'

    def test_registration_incorrect_password(self, browser):
        browser.get(urls.REG_URL)
        browser.find_element(*locators.NAME_REG).send_keys(data.NAME)
        browser.find_element(*locators.EMAIL_REG).send_keys(data.EMAIL_FOR_REG)
        browser.find_element(*locators.PASSWORD_REG).send_keys(data.INC_PASSWORD)
        browser.find_element(*locators.REG_BUTT).click()
        assert 'Некорректный пароль' in browser.find_element(*locators.PASSWORD_ERR).text
