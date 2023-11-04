import pytest
import random

@pytest.fixture
def name():
    return 'vasia'

@pytest.fixture
def email():
    return 'yuliya_levochkina_2@gmail.com'

@pytest.fixture
def password():
    return '12345678'

@pytest.fixture
def inc_password():
    return '123'

@pytest.fixture
def emailforreg():
    return f'vasiaiv{random.randint(100, 999)}@yandex.ru'
