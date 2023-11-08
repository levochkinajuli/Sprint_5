from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    NAME_REG = By.XPATH, "(.//input[@name='name'])[1]"
    EMAIL_REG = By.XPATH, "(.//input[@name='name'])[2]"
    PASSWORD_REG = By.NAME, "Пароль"
    PASSWORD_ERR = By.XPATH, ".//p[text() = 'Некорректный пароль']"
    REG_BUTT = By.XPATH, ".//button[text()='Зарегистрироваться']"


class MainPageLocators:
    BUTT_ENTER_MAIN = By.XPATH, ".//button[text() = 'Войти в аккаунт']"
    BUTT_LK = By.LINK_TEXT, "Личный Кабинет"
    BUTT_ORDER = By.XPATH, ".//button[text() = 'Оформить заказ']"
    BUTT_CONS = By.XPATH, ".//p[text() = 'Конструктор']"
    BUTT_LOGO = By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2"


class LoginPageLocators:
    EMAIL = By.NAME, "name"
    PASSWORD = By.NAME, "Пароль"
    BUTT_ENTER = By.XPATH, ".//button[text() = 'Войти']"
    BUTT_REST_PASS = By.XPATH, ".//a[text() = 'Восстановить пароль']"
    BUTT_ALR_REG = By.XPATH, ".//a[@href='/login']"
    BUTT_LOGOUT = By.XPATH, ".//button[text() = 'Выход']"


class ConstructorLocators:
    BUTT_FILL = By.XPATH, ".//span[contains(text(), 'Начинки')]"
    BUTT_SAU = By.XPATH, ".//span[contains(text(), 'Соусы')]"
    BUTT_BUNS = By.XPATH, ".//span[contains(text(), 'Булки')]"
    FILL_METEOR = By.XPATH, ".//p[text() = 'Говяжий метеорит (отбивная)']"
    SAU_SPICY = By.XPATH, ".//p[text() = 'Соус Spicy-X']"
    BUN_FLU = By.XPATH, ".//p[text() = 'Флюоресцентная булка R2-D3']"



