import allure
import pytest
from estimate_tests.ui.application_manager import app
from estimate_tests.data.data import Users

@pytest.mark.login
@allure.title('TEST: Проверка авторизации пользователя с активной лицензией')
def test_login_valid_user(open_login_page):
    """
        Предусловия:
        Открыта страница логина Сметного офиса
        У пользователя есть активная лицензия
        Шаги:
        1. Ввести логин в поле Логин или email
        2. Ввести пароль в поле Введите пароль
        3. Нажать на кнопку "Начать работу"
        Ожидаемый результат:
        1. Пользователь находится в личном кабинете
        2. Присутствует email пользователя
        3. Присутствует окно "Недавние"
        """
    user = Users.AdminUserPrev()
    app.login_page.click_and_set_login(user.login)\
        .click_and_set_password(user.password)\
        .click_login_button()
    app.account_page.should_be_user_email(user.email)\
        .should_be_recent_window_present()\
        .exit_from_account()
    app.login_page.should_be_login_page_open()\
        .should_be_estimate_office_title()


@pytest.mark.login
@allure.title('TEST: Проверка авторизации пользователя с неправильным паролем')
def test_login_wrong_password(open_login_page):
    """
        Предусловия:
        Открыта страница логина Сметного офиса
        Шаги:
        1. Ввести логин в поле Логин или email
        2. Ввести неправильный пароль в поле Введите пароль
        3. Нажать на кнопку "Начать работу"
        Ожидаемый результат:
        Подсказка "Неверный пароль"
        """
    user = Users.AdminUserPrev()
    app.login_page\
        .click_and_set_login(user.login)\
        .click_and_set_password(user.login)\
        .click_login_button()\
        .should_be_hint_wrong_password()


@pytest.mark.login
@allure.title('TEST: Проверка авторизации пользователя с неправильным логином')
def test_login_wrong_login(open_login_page):
    """
        Предусловия:
        Открыта страница логина Сметного офиса
        Шаги:
        1. Ввести неправильный логин в поле Логин или email
        2. Ввести пароль в поле Введите пароль
        3. Нажать на кнопку "Начать работу"
        Ожидаемый результат:
        Подсказка "Не удалось найти аккаунт"
        """
    user = Users.AdminUserPrev()
    app.login_page\
        .click_and_set_login(user.fake_login)\
        .click_and_set_password(user.password)\
        .click_login_button()\
        .should_be_hint_wrong_login()



@pytest.mark.login
@allure.title('TEST: Проверка авторизации нового пользователя без лицензии')
def test_login_user_without_license(open_login_page):
    """
        Предусловия:
        Открыта страница логина Сметного офиса
        У пользователя нет лицензии
        Шаги:
        1. Ввести логин в поле Логин или email
        2. Ввести пароль в поле Введите пароль
        3. Нажать на кнопку "Начать работу"
        Ожидаемый результат:
        1. Пользователь находится в личном кабинете
        2. Присутствует email пользователя
        3. Кнопка "Перейти к сметам" неактивна
        """
    user = Users.NewUserPrev()
    app.login_page\
        .click_and_set_login(user.login)\
        .click_and_set_password(user.password)\
        .click_login_button()
    app.account_page\
        .should_be_user_email(user.email) \
        .should_be_text_get_license() \
        .should_be_button_go_to_estimate_disabled()\
        .exit_from_account()


@pytest.mark.login
@allure.title('TEST: Проверка авторизации пользователя у которого раньше была лицензия')
def test_login_old_user_without_license(open_login_page):
    """
        Предусловия:
        Открыта страница логина Сметного офиса
        У пользователя нет лицензии
        Шаги:
        1. Ввести логин в поле Логин или email
        2. Ввести пароль в поле Введите пароль
        3. Нажать на кнопку "Начать работу"
        Ожидаемый результат:
        1. Пользователь находится в личном кабинете
        2. Присутствует email пользователя
        3. Таблица с Недавними документами присутствует
        """
    user = Users.NoLicenseUserPrev()
    app.login_page\
        .click_and_set_login(user.login)\
        .click_and_set_password(user.password)\
        .click_login_button()
    app.account_page\
        .should_be_user_email(user.email)\
        .should_be_documents_table_present()\
        .exit_from_account()


@pytest.mark.xfail(reason="broken hint")
@pytest.mark.login
@allure.title('TEST: Проверка авторизации пользователя с пустым паролем')
def test_login_empty_password(open_login_page):
    """
        Предусловия:
        Открыта страница логина Сметного офиса
        У пользователя нет лицензии
        Шаги:
        1. Ввести логин в поле Логин или email
        2. Нажать на кнопку "Начать работу"
        Ожидаемый результат:
        Подсказка: Поле Пароль не может быть пустым
        """
    user = Users.AdminUserPrev()
    app.login_page\
        .click_and_set_login(user.login)\
        .click_and_set_password(user.password)\
        .should_be_hint_password_is_empty()