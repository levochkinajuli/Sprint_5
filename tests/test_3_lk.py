from selenium import webdriver
import time
from locators import EntranceLocators
from conftest import email, password


class TestLoginPage:

    def test_button_lk(self, email, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_lk_button()).click()
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_email_enter()).send_keys(email)
        driver.find_element(*EntranceLocators.locator_password_enter()).send_keys(password)
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_enter_button()).click()
        time.sleep(5)
        driver.find_element(*EntranceLocators.locator_lk_button()).click()
        time.sleep(3)
        assert 'profile' in driver.current_url
        driver.quit()

    def test_from_lk_to_constructor(self, email, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_lk_button()).click()
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_email_enter()).send_keys(email)
        driver.find_element(*EntranceLocators.locator_password_enter()).send_keys(password)
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_enter_button()).click()
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_lk_button()).click()
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_button_constructor()).click()
        assert 'site' in driver.current_url
        driver.quit()

    def test_logout_from_lk(self, email, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_lk_button()).click()
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_email_enter()).send_keys(email)
        driver.find_element(*EntranceLocators.locator_password_enter()).send_keys(password)
        driver.find_element(*EntranceLocators.locator_enter_button()).click()
        time.sleep(2)
        driver.find_element(*EntranceLocators.locator_lk_button()).click()
        time.sleep(2)
        driver.find_element(*EntranceLocators.locator_button_logout()).click()
        time.sleep(2)
        assert 'login' in driver.current_url
        driver.quit()

    def test_from_lk_to_header_logo(self, email, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_lk_button()).click()
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_email_enter()).send_keys(email)
        driver.find_element(*EntranceLocators.locator_password_enter()).send_keys(password)
        driver.find_element(*EntranceLocators.locator_enter_button()).click()
        time.sleep(2)
        driver.find_element(*EntranceLocators.locator_lk_button()).click()
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_logo()).click()
        assert 'site' in driver.current_url
        driver.quit()
