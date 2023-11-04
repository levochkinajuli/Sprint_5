from selenium import webdriver
import time
from locators import EntranceLocators
from conftest import password, email


class TestLoginPage:

    def test_button_entrance(self, email, password):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/login')
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_email_enter()).send_keys(email)
        driver.find_element(*EntranceLocators.locator_password_enter()).send_keys(password)
        driver.find_element(*EntranceLocators.locator_enter_button()).click()
        time.sleep(2)
        assert 'site' in driver.current_url
        driver.quit()

    def test_button_lk(self, password, email):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/')
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_lk_button()).click()
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_email_enter()).send_keys(email)
        driver.find_element(*EntranceLocators.locator_password_enter()).send_keys(password)
        driver.find_element(*EntranceLocators.locator_enter_button()).click()
        assert 'site' in driver.current_url
        driver.quit()

    def test_entrance_button_in_reg_form(self):
        driver = webdriver.Chrome()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        time.sleep(1)
        driver.find_element(*EntranceLocators.locator_entrance_button_already_reg()).click()
        time.sleep(1)
        assert 'site' in driver.current_url
        driver.quit()

    def test_button_forgot_password(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://stellarburgers.nomoreparties.site/login')
        time.sleep(2)
        driver.find_element(*EntranceLocators.locator_restore_password()).click()
        time.sleep(1)
        assert 'forgot-password' in driver.current_url
        driver.quit()
