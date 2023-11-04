from selenium import webdriver
import time
from locators import RegistrationLocators
from conftest import emailforreg, password, inc_password, name


class TestRegistrationPage:

    def test_registration_correct(self, name, emailforreg, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        time.sleep(3)
        driver.find_element(*RegistrationLocators.locator_name()).send_keys(name)
        driver.find_element(*RegistrationLocators.locator_email()).send_keys(emailforreg)
        driver.find_element(*RegistrationLocators.locator_password()).send_keys(password)
        time.sleep(1)
        driver.find_element(*RegistrationLocators.locator_regbutton()).click()
        time.sleep(1)
        assert 'login' in driver.current_url
        driver.quit()

    def test_registration_incorrect_password(self, name, emailforreg, inc_password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        time.sleep(3)
        driver.find_element(*RegistrationLocators.locator_name()).send_keys(name)
        driver.find_element(*RegistrationLocators.locator_email()).send_keys(emailforreg)
        driver.find_element(*RegistrationLocators.locator_password()).send_keys(inc_password)
        driver.find_element(*RegistrationLocators.locator_regbutton()).click()
        time.sleep(2)
        assert 'Некорректный пароль' in driver.find_element(*RegistrationLocators.locator_passworderror()).text
        driver.quit()
