import pytest
from selenium import webdriver
from urls import Urls


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get(Urls.MAIN_URL)

    yield driver
    driver.quit()
