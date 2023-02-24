import time
import allure
from allure_commons.types import Severity, AttachmentType
from selene import command, have
from selene.support.shared import browser
from selene import be
from selenium.webdriver import ActionChains


class ObjectsPage():

    def should_be_my_documents_title_present(self):
        with allure.step('Проверка заголовка Мои документы'):
            browser.element("#rv-hack-div").should(have.text(' Мои документы '))
        allure.attach(browser.driver.get_screenshot_as_png(),
                      name="screen", attachment_type=AttachmentType.PNG)
        with allure.step('Возвращаемся в личный кабинет'):
            browser.element('#ribbon-back-button').should(be.present).click()

        return self

    def open_the_hierarchy_my_estimates(self):
        with allure.step("Раскрываем дерево Мои сметы"):
            my_estimates = browser.element('[aria-node-type="virtual.root"]')
            my_estimates.wait_until(be.clickable)
            my_estimates.double_click()
        allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def create_new_folder(self):
        with allure.step("Клик по кнопке Папка"):
            browser.element("#ribbon-addFolder").should(be.present).click()
            ActionChains(browser.driver).send_keys('Auto').perform()
        return self

    def should_be_new_folder_present(self):
        with allure.step("Проверяем что папка создана"):
            browser.element('[aria-node-type="virtual.root"]').click()
            browser.element('[aria-label="Auto"] [aria-node-type="Folder"]').is_displayed()
            browser.element('//div[contains(text(), "Auto")]').should(be.present)
            allure.attach(browser.driver.get_screenshot_as_png(),
                      name="screen", attachment_type=AttachmentType.PNG)
        if browser.element('[aria-label="Auto"] [aria-node-type="Folder"]').is_displayed():
            browser.element('[aria-label="Auto"] [aria-node-type="Folder"]').context_click()
            browser.element('#context-menu-Delete').click()
            print('Delete data')
        else:
            browser.element('[aria-node-type="virtual.root"]').click()
            print('No data to delete')
        return self

    def click_on_ribbon_paste_tab(self):
        with allure.step("Переход во вкладку Вставка"):
            browser.element('#ribbon-tab-PasteTab').should(be.present).click()
            browser.element('#ribbon-addSection').should(be.visible)
        return self

    def click_on_ribbon_volumes_tab(self):
        with allure.step("Переход во вкладку Объёмы"):
            browser.element('#ribbon-tab-VolumesTab').should(be.present).click()
            browser.element('#ribbon-resetVolume').should(be.visible)
        return self

    def click_on_ribbon_view_tab(self):
        with allure.step("Переход во вкладку Вид"):
            browser.element('#ribbon-tab-ViewTab').should(be.present).click()
            browser.element('#ribbon-setBigTileView').should(be.visible)
        return self

    def click_on_ribbon_operation_tab(self):
        with allure.step("Переход во вкладку Операции"):
            browser.element('#ribbon-tab-OperationTab').should(be.present).click()
            browser.element('#ribbon-numerationSelector').should(be.visible)
        return self

    def click_on_ribbon_report_tab(self):
        with allure.step("Переход во вкладку Отчет"):
            browser.element('#ribbon-tab-ReportTab').should(be.present).click()
            browser.element('#ribbon-saveReport').should(be.visible)
        return self

    def click_on_ribbon_main_tab(self):
        with allure.step("Переход во вкладку Главная"):
            browser.element('#ribbon-tab-MainTab').should(be.present).click()
            browser.element('#ribbon-copy').should(be.visible)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def copy_and_paste_folder(self):
        with allure.step('Скопировать папку'):
            browser.element('[aria-node-type="virtual.root"]').click()
            browser.element('[aria-label="Auto"] [aria-node-type="Folder"]').should(be.present).click()
            browser.element('#ribbon-copy').should(be.present).click()
        with allure.step('Вставить папку'):
            browser.element('#ribbon-paste').should(be.present).click()
            confirmation = browser.element('//div[contains(@class, "p-toast-detail")]')
            confirmation.should(be.visible)
            confirmation.wait_until(be.absent)
        with allure.step('Проверка того что папка успешно вставлена'):
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def click_new_estimate_button(self):
        with allure.step('Создание объекта сметы'):
            browser.element('#ribbon-addEstimate').should(be.present).click()
            browser.element('[aria-label="Новая смета"] [aria-node-type="LocalEstimate"]').wait_until(be.visible)
        return self

    def fill_field_estimate_name(self, value):
        with allure.step('Заполнение поля Наименование сметы'):
            estimate_name = browser.element('#ec-estimate-name')
            estimate_name.wait_until(be.visible)
            estimate_name.click().clear().send_keys(value)
        return self

    def fill_field_object_name(self, value):
        with allure.step('Заполнение поля Наименование объекта'):
            browser.element('#ec-object-name').should(be.present).click().send_keys(value)
        return self

    def fill_field_number_of_estimate(self, value):
        with allure.step('Заполнение поля Номер/шифр сметы'):
            browser.element('#ec-estimate-code').should(be.present).click().send_keys(value)
        return self

    def choose_database_name_sn_from_dropdown(self):
        with allure.step('Выбор базы СН из дропдауна'):
            browser.element('#ec-base-selector').should(be.present).click()
            sn_database_select = browser.element('#ec-base-selector-SN2012_2023')
            sn_database_select.wait_until(be.visible)
            sn_database_select.click()
        return self

    def choose_addition_from_dropdown(self):
        with allure.step('Выбор дополнения из дропдауна'):
            browser.element('#ec-addition-selector').should(be.present).click()
            sn_original_edition = browser.element('#ec-addition-selector-addition-0')
            sn_original_edition.wait_until(be.visible)
            sn_original_edition.click()
        return self

    def click_on_edit_estimate_button(self):
        with allure.step('Клик на кнопку Редактировать смету'):
            browser.element('#edit-estimate-button').click()
        return self

    def should_be_estimate_name_present(self, value):
        with allure.step('Проверяем создана ли смета'):
            browser.element(f'//div[contains(text(), "{value}")]').should(be.present)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def back_to_objects_page(self):
        browser.element('#ribbon-object').should(be.present).click()
        return self

    def choose_database_name_tsn_from_dropdown(self):
        with allure.step('Выбор базы ТСН из дропдауна'):
            browser.element('#ec-base-selector').should(be.present).click()
            sn_database_select = browser.element('#ec-base-selector-TSN_MGE')
            sn_database_select.wait_until(be.visible)
            sn_database_select.click()
        return self

    def choose_addition_tsn_65_from_dropdown(self):
        with allure.step('Выбор дополнения ТСН 65 из дропдауна'):
            browser.element('#ec-addition-selector').should(be.present).click()
            tsn_65 = browser.element('#ec-addition-selector-addition-65')
            tsn_65.wait_until(be.visible)
            tsn_65.click()
            time.sleep(5)
            tsn_mge_build = browser.element('#ec-building-type-selector')
            tsn_mge_build.wait_until(be.enabled)
        return self

    def choose_indexes_tsn_from_dropdown(self):
        with allure.step('Выбор индексов из дропдауна'):
            browser.element('#ec-indexes-year-selector').should(be.present).click()
            year_2022 = browser.element('#ec-indexes-year-selector-2022')
            year_2022.wait_until(be.enabled)
            year_2022.click()
            browser.element('#ec-indexes-month-selector').should(be.present).click()
            month_10 = browser.element('#ec-indexes-month-selector-10-Month')
            month_10.wait_until(be.visible)
            month_10.click()
        return self

    def choose_tsn_chapter_13_from_dropdown(self):
        with allure.step('Выбор ТСН-2001.13 из дропдауна'):
            browser.element('#ec-chapter13-base-selector').should(be.present).click()
            tsn_31_add = browser.element('#ec-chapter13-base-selector-addition-31')
            tsn_31_add.wait_until(be.visible)
            tsn_31_add.click()
        return self

    def choose_indexes_chapter_13_from_dropdawn(self):
        with allure.step('Выбор индексов ТСН-2001.13 из дропдауна'):
            browser.element('#ec-indexes13-year-selector').should(be.present).click()
            year_2021 = browser.element('#ec-indexes13-year-selector-2021')
            year_2021.wait_until(be.visible)
            year_2021.click()
            browser.element('#ec-indexes13-month-selector').should(be.present).click()
            third_quarter = browser.element('#ec-indexes13-month-selector-3-Quarter')
            third_quarter.wait_until(be.visible)
            third_quarter.click()
        return self

    def click_delete_button(self):
        with allure.step('Удаление объекта сметы'):
            browser.element('#ribbon-delete').should(be.present).click()
        return self

    def should_be_estimate_in_trashbox(self):
        with allure.step('Проверка наличия сметы в корзине'):
            browser.element("//div[contains(text(), 'Новая смета')]").click()
            browser.element('[class="banner-contents-label banner-contents-label-big"]'). \
                should(have.text("Смета находится в корзине"))
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def click_on_empty_trash_button(self):
        with allure.step('Очистить корзину'):
            browser.element('[aria-node-type="virtual.recycleBin"]').context_click()
            browser.element('#context-menu-EmptyTrash').click()
        return self

    def should_be_trashbox_is_empty(self):
        with allure.step('Проверяем что корзина пуста'):
            browser.element('[class="banner-contents-label banner-contents-label-big"]') \
                .should(have.text('Здесь скоро будут данные'))
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def click_to_normatives_button(self):
        with allure.step('Перейти в контекст Базы'):
            browser.element('#ribbon-normatives').should(be.present).click()
            browser.element('[mat-focus-indicator ribbon-button mat-raised-button '
                            'mat-button-base toggle-button-checked]').wait_until(be.visible)
        return self
