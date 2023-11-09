from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from data import FirstRegistration
from locators import RegistrationPageLocators,LoginPageLocators
from conftest import browser


class TestRegistrationPage:

    def test_registration_correct(self, browser):
        browser.get(Urls.REG_URL)
        browser.find_element(*RegistrationPageLocators.NAME_REG).send_keys(FirstRegistration.NAME)
        browser.find_element(*RegistrationPageLocators.EMAIL_REG).send_keys(FirstRegistration.EMAIL_FOR_REG)
        browser.find_element(*RegistrationPageLocators.PASSWORD_REG).send_keys(FirstRegistration.PASSWORD)
        browser.find_element(*RegistrationPageLocators.REG_BUTT).click()
        element = LoginPageLocators.BUTT_ENTER
        WebDriverWait(browser, 2).until(expected_conditions.visibility_of_element_located(element))
        assert browser.find_element(*LoginPageLocators.BUTT_ENTER).text == 'Войти'

    def test_registration_incorrect_password(self, browser):
        browser.get(Urls.REG_URL)
        browser.find_element(*RegistrationPageLocators.NAME_REG).send_keys(FirstRegistration.NAME)
        browser.find_element(*RegistrationPageLocators.EMAIL_REG).send_keys(FirstRegistration.EMAIL_FOR_REG)
        browser.find_element(*RegistrationPageLocators.PASSWORD_REG).send_keys(FirstRegistration.INC_PASSWORD)
        browser.find_element(*RegistrationPageLocators.REG_BUTT).click()
        assert 'Некорректный пароль' in browser.find_element(*RegistrationPageLocators.PASSWORD_ERR).text
