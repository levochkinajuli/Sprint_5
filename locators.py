from selenium.webdriver.common.by import By


class RegistrationLocators:
    # Форма регистрации
    #локатор для поля ввода "Имя"
    @staticmethod
    def locator_name():
        name = (By.XPATH, "(.//input[@name='name'])[1]")
        return name

    #локатор для поля ввода Email
    @staticmethod
    def locator_email():
        email = (By.XPATH, "(.//input[@name='name'])[2]")
        return email

    # локатор для поля ввода "Пароль"
    @staticmethod
    def locator_password():
        password = (By.NAME, "Пароль")
        return password

    # локатор для сообщения "Некорректный пароль"
    @staticmethod
    def locator_passworderror():
        passworderror = (By.XPATH, ".//p[text() = 'Некорректный пароль']")
        return passworderror

    # локатор для кнопки "Зарегистрироваться"
    @staticmethod
    def locator_regbutton():
        regbutton = (By.XPATH, ".//button[text()='Зарегистрироваться']")
        return regbutton


class EntranceLocators:

    @staticmethod
    def locator_email_enter():
        email_enter = (By.NAME, "name")
        return email_enter

    @staticmethod
    def locator_password_enter():
        password_enter = (By.NAME, "Пароль")
        return password_enter

    @staticmethod
    def locator_enter_button():
        button = (By.XPATH, ".//button[text() = 'Войти']")
        return button

    @staticmethod
    def locator_lk_button():
        lk = (By.LINK_TEXT, "Личный Кабинет")
        return lk

    @staticmethod
    def locator_entrance_button_already_reg():
        but = (By.XPATH, ".//a[@href='/login']")
        return but

    @staticmethod
    def locator_restore_password():
        but = (By.XPATH, ".//a[text() = 'Восстановить пароль']")
        return but

    @staticmethod
    def locator_button_constructor():
        but = (By.XPATH, ".//p[text() = 'Конструктор']")
        return but

    @staticmethod
    def locator_button_logout():
        but = (By.XPATH, ".//button[text() = 'Выход']")
        return but

    @staticmethod
    def locator_logo():
        logo = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")
        return logo


class Constructor:
    @staticmethod
    def locator_fillings():
        fill = (By.XPATH, ".//span[contains(text(), 'Начинки')]")
        return fill

    @staticmethod
    def locator_sauces():
        sau = (By.XPATH, ".//span[contains(text(), 'Соусы')]")
        return sau

    @staticmethod
    def locator_buns():
        buns = (By.XPATH, ".//span[contains(text(), 'Булки')]")
        return buns

    @staticmethod
    def locator_meteorite():
        meteorite = (By.XPATH, ".//p[text() = 'Говяжий метеорит (отбивная)']")
        return meteorite

    @staticmethod
    def locator_spicy():
        spicy = (By.XPATH, ".//p[text() = 'Соус Spicy-X']")
        return spicy

    @staticmethod
    def locator_bun_flu():
        flu = (By.XPATH, ".//p[text() = 'Флюоресцентная булка R2-D3']")
        return flu
