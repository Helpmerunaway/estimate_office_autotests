import allure
import pytest
from estimate_tests.utils.date_and_time import today_date
from estimate_tests.ui.application_manager import app
from estimate_tests.data.data import TestData

"""

Проверка работы контекста Поиск

"""

@allure.title('TEST: Проверка открытия и закрытия окна поиска')
def test_open_search_window(switch_to_objects_page):
    """"
    Предусловия:
    Пользователь в контексте Поиск
    Шаги:
    1. Открыть окно поиска
    2. Закрыть окно поиска
    Ожидаемое поведение:
    1.Окно открыто
    2. Окно закрыто
    Постусловия:
    """
    app.search_page\
        .click_on_ribbon_search_button()\
        .should_be_search_window_is_present()\
        .click_on_close_window_button()\
        .should_be_search_window_is_absent()


@allure.title('TEST: Проверка результатов поиска по пустому полю')
def test_search_results_by_empty_field(switch_to_search_page):
    """"
    Предусловия:
    Пользователь в контексте Поиск
    Открыто окно Поиск
    Шаги:
    1. Ввести и отправить пустой запрос в поисковую строку
    Ожидаемое поведение:
    Ничего не найдено по вашему запросу
    Постусловия:
    """
    app.search_page\
        .fill_form_search_window(TestData.empty_req)\
        .should_be_nothing_is_find_present()


@allure.title('TEST: Проверка результатов поиска по ключевому слову')
def test_search_results_by_keyword(switch_to_search_page):
    """"
    Предусловия:
    Пользователь в контексте Поиск
    Открыто окно Поиск
    Шаги:
    1. Ввести и отправить запрос в поисковую строку
    Ожидаемое поведение:
    Окно с результатами поиска
    Постусловия:
    """
    app.search_page\
        .fill_form_search_window(TestData.keyword)\
        .should_be_search_results_is_present(TestData.keyword)


@allure.title('TEST: Проверка результатов поиска по обоснованию')
def test_search_results_by_code(switch_to_search_page):
    """"
    Предусловия:
    Пользователь в контексте Поиск
    Открыто окно Поиск
    Шаги:
    1. Ввести и отправить запрос в поисковую строку
    Ожидаемое поведение:
    Окно с результатами поиска
    Постусловия:
    """
    app.search_page\
        .fill_form_search_window(TestData.just_num)\
        .should_be_search_results_is_present(TestData.text_pricing)

