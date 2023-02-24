import allure
from allure_commons.types import Severity, AttachmentType
from selene import command, have
from selene.support.shared import browser
from selene import be


class NormativesPage():

    def should_be_sn_and_tsn_databases_is_present(self):
        with allure.step('СН-2012 Присутствует'):
            sn_2012 = browser.element('[aria-label="Сборник стоимостных нормативов для Москвы СН-2012"]')
            sn_2012.wait_until(be.visible)
            sn_2012.should(be.present)
        with allure.step('ТСН-2001 (МГЭ) Присутствует'):
            tsn_2001 = browser.element('[aria-node-type="NormBaseRoot"]')
            tsn_2001.wait_until(be.visible)
            tsn_2001.should(be.present)
        return self

    def open_collection_sn_2012(self):
        with allure.step('Раскрыть Сборник стоимостных нормативов для Москвы СН-2012'):
            baza_sn = browser.element('[aria-label="Сборник стоимостных нормативов для Москвы СН-2012"] button')
            baza_sn.click()
        return self

    def should_be_current_prices_sn_is_present(self):
        with allure.step('Присутствует СН-2012 в текущих ценах'):
            sn_2012 = browser.all('[aria-node-type="NormBaseRoot"]')\
                .element_by(have.text('СН-2012 (в текущих ценах по состоянию на 01.10.2022 года)'))
            sn_2012.wait_until(be.visible)
            sn_2012.should(be.present)
        return self

    def open_current_prices_sn_2012(self):
        with allure.step('Раскрыть СН-2012 в текущих ценах'):
            browser.element('[aria-label="СН-2012 (в текущих ценах по состоянию на 01.10.2022 года)"] button')\
                .should(be.present).click()
        return self

    def should_be_normatives_and_corrections_sn_is_present(self):
        with allure.step('Присутствуют Нормативы'):
            normatives = browser.element('[aria-node-type="NormativesVirtual"]')
            normatives.wait_until(be.visible)
            normatives.should(be.present)
        with allure.step('Присутствуют поправки'):
            corrections = browser.element('[aria-node-type="CorrectionsRoot"]')
            corrections.wait_until(be.visible)
            corrections.should(be.present)
        return self

    def open_collection_tsn_2001_mge(self):
        with allure.step('Раскрыть Территориальные сметные нормативы для Москвы ТСН-2001 (МГЭ)'):
            baza_tsn = browser.element\
                ('[aria-label="Территориальные сметные нормативы для Москвы ТСН-2001 (МГЭ)"] button')
            baza_tsn.click()
        return self

    def should_be_tsn_2001_and_tsn_13_chapter_is_present(self):
        with allure.step('Присутствует ТСН-2001 (МГЭ)'):
            tsn_2001 = browser.all('[aria-node-type="NormBaseRoot"]')\
                .element_by(have.text('ТСН-2001 (МГЭ)'))
            tsn_2001.wait_until(be.visible)
            tsn_2001.should(be.present)
        with allure.step('Присутствует ТСН-2001. Глава 13.'):
            tsn_13_chapter = browser.all('[aria-node-type="NormBaseRoot"]')\
                .element_by(have.text('ТСН-2001 (МГЭ). Глава 13'))
            tsn_13_chapter.wait_until(be.visible)
            tsn_13_chapter.should(be.present)
        return self

    def open_tsn_2001_mge(self):
        with allure.step('Раскрыть ТСН-2001 (МГЭ)'):
            tsn_2001_mge = browser.element('[aria-label="ТСН-2001 (МГЭ)"] button')
            tsn_2001_mge.wait_until(be.visible)
            tsn_2001_mge.click()
        return self

    def should_be_normo_indexes_and_corrections_tsn_is_present(self):
        with allure.step('Присутствуют Нормативы, Индексы и Поправки'):
            normo = browser.all('[aria-node-type="NormativesVirtual"]').element_by(have.text('Нормативы'))
            normo.wait_until(be.visible)
            normo.should(be.present)
            indexes = browser.all('[aria-node-type="IndexesRoot"]').element_by(have.text('Индексы'))
            indexes.wait_until(be.visible)
            indexes.should(be.present)
            correction = browser.all('[aria-node-type="CorrectionsRoot"]').element_by(have.text('Поправки'))
            correction.wait_until(be.visible)
            correction.should(be.present)
        return self

    def open_normatives(self):
        with allure.step('Раскрыть Нормативы'):
            norma = browser.element('[aria-label="Нормативы"] button')
            norma.wait_until(be.visible)
            norma.click()
        return self
    
    def should_be_normative_code_is_present(self, add_num):
        with allure.step('Нормативы ТСН присутствуют'):
            addition = browser.all('[aria-node-type="NormativesRoot"]').element_by(have.text(add_num))
            addition.wait_until(be.visible)
            addition.should(be.present)
        return self

    def open_addition_65_tsn(self):
        with allure.step('Раскрыть Дополнение 65'):
            addition = browser.element('[aria-label="Дополнение 65"] button')
            addition.wait_until(be.clickable)
            addition.click()
        return self

    def should_be_chapter_one_is_present(self):
        with allure.step('Присутствует Глава 1.'):
            chapter_one = browser.all('[aria-node-type="ResourcesVolume"]').element_by\
                (have.text('Глава 1. Средние сметные цены на материалы, изделия и конструкции'))
            chapter_one.wait_until(be.visible)
            chapter_one.should(be.present)
        return self

    def open_chapter_one_tsn(self):
        with allure.step('Открыть Главу 1.'):
            chapter_one = browser.element(
                '[aria-label="Глава 1. Средние сметные цены на материалы, изделия и конструкции"] button')
            chapter_one.wait_until(be.visible)
            chapter_one.click()
        return self

    def should_be_section_one(self):
        with allure.step('Присутствует Раздел 1.'):
            section_one = browser.all('[class="p-treenode-label"] [aria-node-type="Materials"]')[1]\
                .should(have.text('Раздел 1. Материалы строительные, дорожные и для реставрационно-восстановительных работ'))
            section_one.should(be.present)
            return self

    def click_on_section_one(self):
        with allure.step('Клик на Раздел 1.'):
            section_one = browser.all('[aria-node-type="Materials"]')\
                .element_by(have.text('Раздел 1. Материалы строительные, дорожные и для реставрационно-восстановительных работ'))
            section_one.click()
        return self

    def should_be_material_on_grid_is_present(self, material):
        with allure.step('Присутствует материал в гриде'):
            mat = browser.all('[class="ss-cell-name-column"]').element_by(have.text(material))
            mat.wait_until(be.visible)
            mat.should(be.present)
        return self

    def click_on_techpart_button(self):
        with allure.step('Клик на кнопку техническая часть'):
            techpart = browser.all('[class="mat-tab-label-content"]').element_by(have.text('Техническая часть'))
            techpart.wait_until(be.visible)
            techpart.click()
        return self

    def should_be_section_one_techpart_tsn_is_present(self):
        with allure.step('Техчасть открыта'):
            techpart_iframe = browser.element('div [class="iframe-doc"]')
            techpart_iframe.wait_until(be.visible)
            techpart_iframe.should(be.present)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def should_be_section_one_techpart_sn_is_present(self):
        with allure.step('Техчасть открыта'):
            techpart = browser.element('[class="frame-wrapper"]')
            techpart.wait_until(be.visible)
            techpart.should(be.present)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self


    def open_indexes(self):
        with allure.step('Раскрыть Индексы'):
            index = browser.element('[aria-label="Индексы"] button')
            index.wait_until(be.visible)
            index.click()
        return self

    def should_be_indexes_is_present(self):
        with allure.step('Присутствуют Индексы за 2022'):
            year2022 = browser.all('[aria-label="2022"]').element_by(have.text('2022'))
            year2022.wait_until(be.visible)
            year2022.should(be.present)
        return self

    def open_year_2022(self):
        with allure.step('Раскрыть Индексы за 2022'):
            year = browser.element('[aria-label="2022"] button')
            year.wait_until(be.visible)
            year.click()
        return self

    def should_be_indexes_month_is_present(self,month):
        with allure.step(f'Присутствуют индесы за {month} 2022'):
            index_month = browser.all('[aria-node-type="IndexesRegistry"]').element_by(have.text(month))
            index_month.wait_until(be.visible)
            index_month.should(be.present)
        return self

    def click_on_month(self, month):
        with allure.step('Клик на индексы'):
            index_month = browser.all('[aria-node-type="IndexesRegistry"]').element_by(have.text(month))
            index_month.wait_until(be.visible)
            index_month.click()
        return self

    def should_be_indexes_grid_is_present(self):
        with allure.step('Открыта таблица с индексами'):
            browser.element('[col-id="InflMaterials"]').wait_until(be.visible)
            browser.element('[col-id="InflMaterials"]').should(have.text('МР'))
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def open_corrections(self):
        with allure.step('Раскрыть Поправки'):
            corr = browser.element('[aria-label="Поправки"] button')
            corr.wait_until(be.visible)
            corr.click()
        return self

    def should_be_corrections_is_present(self, corr):
        with allure.step(f'Присутствуют {corr}'):
            correction = browser.all('[aria-node-type="CorrectionRegistry"]').element_by(have.text(corr))
            correction.wait_until(be.visible)
            correction.should(be.present)
        return self

    def click_on_correction_name(self, corr):
        with allure.step('Клик на поправки'):
            corr_name = browser.all('[aria-node-type="CorrectionRegistry"]').element_by(have.text(corr))
            corr_name.wait_until(be.visible)
            corr_name.click()
        return self

    def should_be_corrections_code_is_present(self, corr_code):
        with allure.step('Поправки присутствуют'):
            correction_code = browser.all('[col-id="pressmarkCol"]').element_by(have.text(corr_code))
            correction_code.wait_until(be.visible)
            correction_code.should(be.present)
            allure.attach(browser.driver.get_screenshot_as_png(),
                          name="screen", attachment_type=AttachmentType.PNG)
        return self

    def should_be_sn_normative_is_present(self, add_num):
        with allure.step('Норматив СН присутствует'):
            addition = browser.all('[aria-node-type="NormativesRoot"]').element_by(have.text(add_num))
            addition.wait_until(be.visible)
            addition.should(be.present)
        return self

    def open_addition_first_sn(self):
        with allure.step('Раскрыть Первоначальное издание'):
            addition = browser.element('[aria-label="Первоначальное издание"] button')
            addition.wait_until(be.clickable)
            addition.click()
        return self

    def should_be_chapter_one_sn_is_present(self):
        with allure.step('Присутствует Глава 1.'):
            chapter_one = browser.all('[aria-node-type="NormativesVolume"]').element_by\
                (have.text('1. Здания'))
            chapter_one.wait_until(be.visible)
            chapter_one.should(be.present)
        return self

    def open_chapter_one_sn(self):
        with allure.step('Открыть Главу 1.'):
            chapter_one = browser.element(
                '[aria-label="1. Здания"] button')
            chapter_one.wait_until(be.visible)
            chapter_one.click()
        return self

    def should_be_section_one_sn(self):
        with allure.step('Присутствует Раздел 1.'):
            section_one = browser.all('[class="p-treenode-label"] [aria-node-type="Normatives"]')[0]\
                .should(have.text('1 - Земляные работы'))
            section_one.should(be.present)
            return self

    def click_on_section_one_sn(self):
        with allure.step('Клик на Раздел 1.'):
            section_one = browser.all('[aria-node-type="Normatives"]')\
                .element_by(have.text('1 - Земляные работы'))
            section_one.click()
        return self
