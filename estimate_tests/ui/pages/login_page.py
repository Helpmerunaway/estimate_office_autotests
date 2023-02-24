import allure
from allure_commons.types import Severity, AttachmentType
from selene import command, have
from selene.support.shared import browser

from estimate_tests.ui.conftest import preview_link


class LoginPage():

    def click_and_set_login(self, value):
        with allure.step('Клик по полю логин'):
            browser.element('#login-input').click()
        with allure.step('Заполнить кнопку логин'):
            browser.element('#login-input').type(value)
        return self

    def click_and_set_password(self, value):
        with allure.step('Клик по полю пароль'):
            browser.element('#password-input').click()
        with allure.step('Заполнить поле логин'):
            browser.element('#password-input').type(value)
        return self

    def click_login_button(self):
        with allure.step('Клик по кнопке Начать работу'):
            browser.element('#login-button').click()
        return self

    def should_be_login_page_open(self):
        with allure.step('Должна быть открыта страница логина'):
            assert 'login' in browser.driver.current_url, f"Wrong URL, must be {preview_link}"
        return self

    def should_be_estimate_office_title(self):
        with allure.step('Должен присутствовать заголовок'):
            assert 'Сметный офис' in browser.driver.title, "This is not a login page"
        return self

    def should_be_hint_wrong_password(self):
        with allure.step('Проверяем наличие подсказки "Неверный пароль"'):
            browser.all('#mat-error-1').should(have.text('Неверный пароль'))
            allure.attach(browser.driver.get_screenshot_as_png(),
                        name="screen", attachment_type=AttachmentType.PNG)
        return self

    def should_be_hint_wrong_login(self):
        with allure.step('Проверяем наличие подсказки "Не удалось найти аккаунт"'):
            browser.all('#mat-error-0').should(have.text('Не удалось найти аккаунт'))
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def should_be_hint_password_is_empty(self):
        with allure.step('Проверяем наличие подсказки "Поле Пароль не может быть пустым"'):
            browser.element('#password-input').clear()
            browser.element("//mat-error[contains(@class, 'mat-error')]")\
                .should(have.text('Поле "Пароль" не может быть пустым'))
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self