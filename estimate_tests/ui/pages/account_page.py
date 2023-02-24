import allure
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import command, have, be
from selene.support.shared import browser


class AccountPage():

    def should_be_user_email(self, value):
        with allure.step("Присутствует емейл пользователя"):
            browser.element('.user-email').should(have.text(value))
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def should_be_recent_window_present(self):
        with allure.step('Проверяем наличие окна "Недавние"'):
            browser.all('.documents-wrapper').should(have.text('Недавние (последние 10 смет)'))
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def exit_from_account(self):
        with allure.step('Клик по кнопке Меню пользователя'):
            browser.element("#heared-user-block").should(be.present).click()
        with allure.step('Выход из личного кабинета'):
            browser.element("#header-dropdown-logout").should(be.present).click()
        return self

    def should_be_text_get_license(self):
        with allure.step("Должен присутствовать текст 'Приобрести лицензию'"):
            browser.element("span[class='mat-button-wrapper']").should(have.text('ПРИОБРЕСТИ ЛИЦЕНЗИЮ'))
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def should_be_button_go_to_estimate_disabled(self):
        with allure.step("Кнопка 'Перейти к смете' неактивна"):
            browser.element("#go-to-estimates-button") \
                .should(be.disabled)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def should_be_documents_table_present(self):
        with allure.step('Таблица с документами присутствует'):
            browser.element('#documents-table').should(be.present)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def should_be_button_go_to_estimate_enabled(self):
        with allure.step("Кнопка 'Перейти к сметам' активна"):
            browser.element("#go-to-estimates-button") \
                .should(be.enabled)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def click_go_to_estimates_button(self):
        with allure.step('Клик по кнопке Перейти к сметам'):
            browser.element("#go-to-estimates-button").should(be.present).click()
        return self

    def click_on_license_manager_button(self):
        with allure.step("Клик на Менеджер лицензий"):
            browser.element('#menu-item-licenseManager').should(be.present).click()
        return self

    def should_be_license_manager_header(self):
        with allure.step("Проверяем наличие заголовка Менеджер лицензий"):
            browser.all('//div[contains(@class, "tab-header")]').should(have.text('Менеджер лицензий'))
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def click_on_help_about_program(self):
        with allure.step('Клик по кнопке "Справка о программе"'):
            browser.element('#menu-item-about-program').should(be.present).click()
        return self

    def should_be_quick_start_page_open(self):
        with allure.step('Проверка открытия "Справки о программе"'):
            browser.switch_to_next_tab()
            browser.element('.md-content #_1').should(be.present).should(have.text('Быстрый старт работы в '))
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
            browser.close_current_tab()
            browser.switch_to_tab(0)
        return self

    def click_on_about_program_button(self):
        with allure.step('Клик на блок пользователя'):
            browser.element("#heared-user-block").should(be.present).click()
            browser.element('#header-dropdown-about-program').should(be.present).click()
        return self

    def should_be_about_program_window_present(self):
        with allure.step('Окно "О программе" открыто'):
            browser.element('[class="window-content"]').should(be.present)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        with allure.step('Закрываем окно'):
            browser.element('div .window-close-button-icon').should(be.present).click()
        return self

