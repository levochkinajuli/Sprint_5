#Sprint_5
Проект автоматизации тестирования сервиса Stellar Burgers
Основа для написания автотестов — фреймворк pytest

Проверка следующего функционала:

1. Регистрация
1.1.Успешная регистрация. 
Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru. 
Минимальный пароль — шесть символов.
1.2. Ошибку для некорректного пароля.

2. Вход
2.1. Вход по кнопке «Войти в аккаунт» на главной,
2.2. Вход через кнопку «Личный кабинет»,
2.3. Вход через кнопку «Войти» в форме регистрации,
2.4. Вход через кнопку в форме восстановления пароля.

3. Переход в личный кабинет 
3.1. Переход по клику на «Личный кабинет».
3.2. Переход из личного кабинета в конструктор.
3.3. Переход по клику на «Конструктор» 
3.4. Переход по кликуна логотип Stellar Burgers.
3.5. Выход из аккаунта
Выход по кнопке «Выйти» в личном кабинете.

4. «Конструктор»
Переходы к разделам:
«Булки»,
«Соусы»,
«Начинки».
