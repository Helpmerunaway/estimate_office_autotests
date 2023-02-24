import time

import allure
from allure_commons.types import Severity, AttachmentType
from selene import command, have
from selene.support.shared import browser
from selene import be
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class EstimatesPage():

    def click_on_pastetab_button(self):
        with allure.step('Клик по батону "Вставка"'):
            paste_tab = browser.element('#ribbon-tab-PasteTab')
            paste_tab.wait_until(be.clickable)
            paste_tab.click()
            browser.element('#ribbon-addPrice').matching(be.clickable)
        return self

    def click_on_button_addprice(self):
        with allure.step('Клик по батону "Расценка"'):
            add_price = browser.element('#ribbon-addPrice')
            add_price.wait_until(be.clickable)
            add_price.click()
        return self

    def should_be_pricing_is_present(self):
        with allure.step('Проверяем что расценка №1 добавлена в смету'):
            pricing = browser.all('[role="gridcell"][col-id="viewNumber"]')[1]
            pricing.should(be.present)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
            pricing.click()
        return self

    def click_on_delete_button(self):
        with allure.step('Удаляем расценку'):
            browser.element('#ribbon-tab-MainTab').click()
            delete_button = browser.element('#ribbon-delete')
            delete_button.wait_until(be.clickable)
            delete_button.click()
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def click_on_pressmark_and_recall(self, value):
        with allure.step('Клик по строке'):
            just = browser.element('[role="gridcell"][col-id="pressmark"] [class="pressmark-comp-wrapper"]')
            just.wait_until(be.clickable)
            just.click()
        with allure.step('Ввод и перевызов обоснования'):
            time.sleep(2)
            ActionChains(browser.driver).send_keys(value).key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(
                Keys.CONTROL).perform()
        return self

    def should_be_correct_text_present(self):
        with allure.step('Проверяем что перевызов выполнен'):
            name_text = browser.all('.name-comp-wrapper [class="text-area"]')[2]
            name_text.wait_until(be.visible)
            name_text.should(have.text(
                'Облицовка стен гранитными плитами полированными толщиной 40 мм при числе плит в 1 м2 до 2'))
            browser.elements('div').element_by(have.text(
                'Облицовка стен гранитными плитами полированными толщиной 40 мм при числе плит в 1 м2 до 2'))
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    # TODO: refactor
    def unbundling_a_resource(self, value):
        with allure.step('Разукрупнение ресурса'):
            material_resource = browser.all('[col-id="pressmark"]').element_by(have.text(value))
            material_resource.wait_until(be.clickable)
            material_resource.click()
            ActionChains(browser.driver).key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()
            browser.element('[class="window-header window-header-background ng-star-inserted"]').should(be.present)
        return self

    def choose_resource_from_modal(self, value):
        with allure.step('Выбор ресурса из модального окна'):
            resource_modal = browser.all('[col-id="priceCode"]').element_by(have.text(value))
            resource_modal.wait_until(be.clickable)
            resource_modal.click()
            choose_button = browser.element(
                "[class='mat-focus-indicator button mat-raised-button mat-button-base mat-primary ng-star-inserted']")
            choose_button.wait_until(be.clickable)
            choose_button.click()
        return self

    def should_be_unbundled_resource_is_present(self, value):
        with allure.step('Разукрупненный ресурс присутствует на странице'):
            loader = browser.element('[class="spinner-wrapper ng-star-inserted"]')
            loader.wait_until(be.absent)
            resource_unbundled = browser.all('[col-id="pressmark"]').element_by(have.text(value))
            resource_unbundled.wait_until(be.visible)
            resource_unbundled.matching(be.present)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def should_be_zero_estimate_cost(self):
        with allure.step('Проверяем итоги по смете'):
            # estimate_totals_footer = browser.all('[mattooltipclass="estimate-tab-tooltip"]').element_by(have.text('0,00'))
            # estimate_totals_footer.wait_until(be.visible)
            # estimate_totals_footer.should(be.present)
            # cena = browser.element('[col-id="totalInBasePrice"] '
            #                        '[class="formula-cell formula-cell-default default-cell ng-star-inserted"]')
            # cena.should(have.text('0,00'))
            estimate_total = browser.all('[col-id="totalInBasePrice"]').element_by(have.text('0,00'))
            estimate_total.wait_until(be.visible)
            estimate_total.should(be.present)
        return self

    def enter_value_of_pricing(self, value):
        with allure.step('Вводим объем у расценки'):

            browser.element('[col-id="powerOne"] [class="power-text"]').should(be.present).click()
            ActionChains(browser.driver).send_keys(value).send_keys(Keys.ENTER).perform()
        return self

    def should_be_correct_value_of_pricing(self, price):
        with allure.step('Проверяем что объем введен'):
            browser.element('[col-id="powerOne"] [class="power-text"]').should(have.text(price))
        return self

    def should_be_correct_estimate_cost(self):
        with allure.step("Итоги по смете должны быть верные"):
            # estimate_totals_footer = browser.all('[mattooltipclass="estimate-tab-tooltip"]').element_by(
            #     have.text('4 915 950,19 ₽'))
            # estimate_totals_footer.wait_until(be.visible)
            # estimate_totals_footer.should(be.present)
            # cena = browser.element('[col-id="totalInBasePrice"] '
            #                        '[class="formula-cell formula-cell-default default-cell ng-star-inserted"]')
            # cena.should(have.text('4 915 950,19 ₽'))
            estimate_total = browser.all('[col-id="totalInBasePrice"]').element_by(have.text('4 915 950,19 ₽'))
            estimate_total.wait_until(be.visible)
            estimate_total.should(be.present)
        return self

    def click_on_search_button(self):
        with allure.step('Клик на кнопку Поиск'):
            browser.element('#ribbon-search').should(be.visible).click()
        return self

    def should_be_search_window_is_present(self):
        with allure.step('Проверка Открылось ли окно поиска'):
            search_window = browser.element('[class="window-header window-header-background ng-star-inserted"]')
            search_window.wait_until(be.visible)
            search_window.matching(be.present)
        return self

    def click_and_type_search(self, word):
        with allure.step('Клик по полю поиск'):
            search = browser.element('[type="search"]')
            search.wait_until(be.visible)
            search.click()
        with allure.step('Поиск по ключевому слову'):
            search.send_keys(word).press_enter()
            spinner = browser.element('[class="spinner-container ng-star-inserted"]')
            spinner.wait_until(be.absent)
        return self

    def copy_normative(self):
        with allure.step('Копировать норматив'):
            obosnovanie = browser.all('[role="gridcell"][col-id="titleNormCol"]')[0]
            obosnovanie.click()
            browser.element('//div[contains(text(), "6.53-16-2")]').context_click()
            browser.element('#eName').click()
        return self

    def close_search_window(self):
        with allure.step('Закрыть окно поиска'):
            browser.element('[class="window-close-button"]').should(be.present).click()
        return self

    def context_click_on_chapter_one(self):
        with allure.step('Клик по Разделу 1'):
            browser.element('//div[contains(text(), "Раздел 1.")]').should(be.present).context_click()
        return self

    def paste_normative_into_estimate(self):
        with allure.step('Вставить скопированный норматив'):
            browser.element('#context-menu-pasteRecord').should(be.present).click()
            loader = browser.element('[class="spinnerWrapper"]')
            loader.wait_until(be.absent)
        return self

    def should_be_correct_pricing_is_present(self, value):
        with allure.step('Обоснование присутствует на странице'):
            loader = browser.element('[class="spinnerWrapper"]')
            loader.wait_until(be.absent)
            resource_unbundled = browser.all('[col-id="pressmark"]').element_by(have.text(value))
            resource_unbundled.wait_until(be.visible)
            resource_unbundled.matching(be.present)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def click_on_pricing(self, text):
        with allure.step('Клик на обоснование'):
            pricing = browser.all('[col-id="name"]').element_by(have.text(text))
            pricing.click()
        return self

    def click_on_maintab_copy_button(self):
        with allure.step('Скопировать расценку'):
            browser.element('#ribbon-tab-MainTab').should(be.present).click()
            browser.element('#ribbon-copy').should(be.present).click()
        return self

    def click_on_maintab_paste_button(self):
        with allure.step('Вставить расценку'):
            browser.element('#ribbon-tab-MainTab').should(be.present).click()
            browser.element('#ribbon-paste').should(be.visible).click()
        return self

    def should_be_pasted_pricing_is_present(self, text):
        with allure.step('Проверяем что расценка вставлена'):
            name_text = browser.all('[class="text-area"]')[1]
            name_text.should(have.text(text))
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
            pasted_pricing = browser.all('[col-id="viewNumber"]').element_by(have.text('2'))
            pasted_pricing.wait_until(be.visible)
            pasted_pricing.matching(be.present)
        return self

    def click_on_add_new_section_button(self):
        with allure.step('Клик по батону "Раздел"'):
            browser.element('#ribbon-addSection').should(be.present).click()
        return self

    def should_be_new_section_is_present(self):
        with allure.step('Проверяем что новый раздел присутствует'):
            new_section = browser.element('//div[contains(text(), "Новый раздел")]')
            new_section.wait_until(be.visible)
            new_section.should(be.present)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def click_on_add_material_button(self):
        with allure.step('Клик по батону "Материал"'):
            add_material = browser.element('#ribbon-addMaterial')
            add_material.wait_until(be.clickable)
            add_material.click()
            time.sleep(5)
        return self

    def fill_fields_justification_and_name(self, number, text):
        with allure.step('Заполняем Обоснование'):
            material = browser.element('[col-id="pressmark"] [class="text-area"]')
            material.wait_until(be.present)
            ActionChains(browser.driver).send_keys(number).send_keys(Keys.TAB).perform()
        with allure.step('Заполняем Наименование'):
            ActionChains(browser.driver).send_keys(text).send_keys(Keys.ENTER).perform()
        return self

    def should_be_line_is_present(self, value):
        with allure.step("Проверяем что строка присутствует на странице"):
            material = browser.all('[col-id="name"]').element_by(have.text(value))
            material.wait_until(be.visible)
            material.should(be.present)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def click_on_add_equipment_button(self):
        with allure.step('Клик по батону "Оборудование"'):
            add_equipment = browser.element('#ribbon-addEquipment')
            add_equipment.wait_until(be.clickable)
            add_equipment.click()
            time.sleep(5)
        return self

    def should_be_comment_is_present(self, value):
        with allure.step("Проверяем что строка присутствует на странице"):
            comment = browser.all('[col-id="viewNumber"]').element_by(have.text(value))
            comment.wait_until(be.visible)
            comment.should(be.present)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def click_on_add_machine_button(self):
        with allure.step('Клик по батону "Оборудование"'):
            add_equipment = browser.element('#ribbon-addMachines')
            add_equipment.wait_until(be.clickable)
            add_equipment.click()
            time.sleep(5)
        return self

    def click_on_add_comment_button(self):
        with allure.step('Клик по батону Комментарий'):
            add_comment = browser.element('#ribbon-addComment')
            add_comment.wait_until(be.clickable)
            add_comment.click()
            time.sleep(5)
        return self

    def rename_comment(self, text):
        with allure.step("Заполняем наименование"):
            comment = browser.all('[col-id="viewNumber"]').element_by(have.text('Комментарий'))
            comment.wait_until(be.visible)
            comment.click()
            ActionChains(browser.driver).send_keys(text).send_keys(Keys.ENTER).perform()
        return self

    def context_click_on_pricing(self, value):
        with allure.step('Контекстный клик на расценке'):
            just = browser.all('[role="gridcell"][col-id="pressmark"] [class="text-area"]')\
                .element_by(have.text(value))
            just.wait_until(be.clickable)
            just.context_click()
        return self

    def click_jump_to_normo_from_context_menu(self):
        with allure.step('Переход к нормативу через контекстное меню'):
            browser.element('#context-menu-jumpToNormoContext').should(be.visible).click()
        return self

    def should_be_normative_on_grid(self):
        with allure.step("Проверяем что норматив присутствует"):
            normative = browser.all('[role="gridcell"][col-id="titleNormCol"]')[2]
            normative.wait_until(be.visible)
            normative.should(have.text(
                'Облицовка стен гранитными плитами полированными толщиной 40 мм при числе плит в 1 м2 до 2'))
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def click_open_tech_doc_from_context_menu(self):
        with allure.step('Открыть техчасть через контекстное меню'):
            browser.element('#context-menu-openTechDoc').should(be.visible).click()
        return self

    def should_be_correct_tech_doc_is_open(self):
        with allure.step('Открыта техчасть'):
            browser.element('//div[contains(text(), "3.15-1-1")]').should(be.present)
        with allure.step('Закрываем окно с техчастью'):
            browser.element("[class='window-close-button']").should(be.visible).click()
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

