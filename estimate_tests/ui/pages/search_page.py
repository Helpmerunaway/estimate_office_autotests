import allure
from selene import command, have
from selene.support.shared import browser
from selene import be
from selenium.webdriver.common.keys import Keys


class SearchPage():

    def click_on_ribbon_search_button(self):
        with allure.step("Клик на кнопку Поиск"):
            browser.element('#ribbon-search').should(be.clickable).click()
            browser.element('[class="window-smr"] [class="content-wrapper"]').wait_until(be.visible)
        return self

    def should_be_search_window_is_present(self):
        with allure.step('Присутствует окно Поиска'):
            browser.element('[class="window-smr"] [class="content-wrapper"]').should(be.visible)
            browser.element('[class="window-header window-header-background ng-star-inserted"]')\
                .should(have.text('Поиск'))
        return self

    def click_on_close_window_button(self):
        with allure.step('Клик на кнопку закрыть окно поиск'):
            browser.element('[class="window-close-button"]').should(be.visible).click()
        return self

    def should_be_search_window_is_absent(self):
        with allure.step('Окно Поиск отсутствует'):
            browser.element('[class="window-smr"] [class="content-wrapper"]').should(be.absent)
        return self

    def fill_form_search_window(self, value):
        with allure.step('Заполнение поле поиска и клик ENTER'):
            search = browser.element('[type="search"]')
            search.wait_until(be.visible)
            search.click().send_keys(value).send_keys(Keys.ENTER)
        return self

    def should_be_search_results_is_present(self, result):
        with allure.step('Присутствует результат запроса'):
            results = browser.element('[class="ss-cell-name-column"]')
            results.wait_until(be.visible)
            results.should(have.text(result))
        return self

    def should_be_nothing_is_find_present(self):
        with allure.step('Присутствует запись "Ничего не найдено"'):
            res = browser.element('[class="no-result-container ng-star-inserted"]')
            res.wait_until(be.visible)
            res.should(have.text('Ничего не найдено по Вашему запросу. Попробуйте поискать что-то другое.'))
        return self
