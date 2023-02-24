import allure
import pytest
from estimate_tests.data.data import TestData
from estimate_tests.data.data import Users
from estimate_tests.ui.application_manager import app


@pytest.mark.account
@allure.title('TEST: Email пользователя отображается в личном кабинете')
def test_account_email_is_present(auth_user):
    """
        Предусловия:
        Пользователь с лицензией авторизовался на сайте
        Ожидаемый результат:
        1. Пользователь находится в личном кабинете
        2. Присутствует email пользователя
        """
    user = Users.AdminUserPrev()
    app.account_page\
        .should_be_user_email(user.email)\



@pytest.mark.account
@allure.title('TEST: Кнопка "Перейти к сметам" активна')
def test_account_go_to_estimate_button(auth_user):
    """
        Предусловия:
        Пользователь с лицензией авторизовался на сайте
        Ожидаемый результат:
        1. Пользователь находится в личном кабинете
        2. Кнопка "Перейти к сметам" активна
        """
    app.account_page\
        .should_be_button_go_to_estimate_enabled()


@pytest.mark.account
@allure.title('TEST: Переход к сметам')
def test_account_enter_objects_page(auth_user):
    """
        Предусловия:
        Пользователь с лицензией авторизовался на сайте
        Шаги:
        1. Нажать на кнопку "Перейти к сметам"
        Ожидаемый результат:
        1. Выполнен переход на страницу Сметы
        2. Присутствует заголовок "Мои документы"
        Постусловия:
        Возвращаемся в личный кабинет
        """
    app.account_page\
        .click_go_to_estimates_button()
    app.objects_page\
        .should_be_my_documents_title_present()



@pytest.mark.account
@allure.title('TEST: Проверка перехода в "Менеджер лицензий"')
def test_account_license_manager(auth_user):
    """
        Предусловия:
        Пользователь с лицензией авторизовался на сайте
        Шаги:
        1. Нажать на кнопку "Менеджер лицензий"
        Ожидаемый результат:
        1. Присутствует заголовок "Менеджер лицензий"
        Постусловия:
        Вернуться в личный кабинет
        """
    app.account_page\
        .click_on_license_manager_button()\
        .should_be_license_manager_header()


@pytest.mark.account
@allure.title('TEST: Проверка перехода в "Справка о программе"')
def test_account_help_about_the_program(auth_user):
    """
        Предусловия:
        Пользователь с лицензией авторизовался на сайте
        Шаги:
        1. Нажать на кнопку "Справка о программе"
        Ожидаемый результат:
        1. В новом окне открылась справка "Быстрый старт"
        Постусловия:
        Закрыть окно Быстрый старт
        """
    app.account_page\
        .click_on_help_about_program()\
        .should_be_quick_start_page_open()

@pytest.mark.account
@allure.title('TEST: Проверка открытия "О программе"')
def test_account_open_about_program(auth_user):
    """
        Предусловия:
        Пользователь с лицензией авторизовался на сайте
        Шаги:
        1. Нажать на email пользователя
        2. Нажать на кнопку "О программе"
        Ожидаемый результат:
        1. Открылось окно "О программе"
        Постусловия:
        Закрыть окно "О программе"
        """
    app.account_page\
        .click_on_about_program_button()\
        .should_be_about_program_window_present()






