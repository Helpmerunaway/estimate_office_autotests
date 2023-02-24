import allure
import pytest
from estimate_tests.utils.date_and_time import today_date
from estimate_tests.ui.application_manager import app
from estimate_tests.data.data import TestData

"""

Проверка работы контекста Базы

"""


@allure.title('TEST: Проверка наличия Нормативов и Поправок у Базы СН 2012')
def test_open_database_sn_2012(switch_to_database_page):
    """"
    Предусловия:
    Пользователь в контексте Базы
    Шаги:
    1. Раскрыть сборник стоимостных нормативов для Москвы СН-2012
    2. Раскрыть СН-2012 (в текущих ценах по состоянию на 01.10.2022 года)
    Ожидаемое поведение:
    1. Присутствуют сборники СН-2012
    2. Присутствуют Нормативы и Поправки СН-2012
    Постусловия:
    """
    app.normatives_page\
        .should_be_sn_and_tsn_databases_is_present()\
        .open_collection_sn_2012()\
        .should_be_current_prices_sn_is_present()\
        .open_current_prices_sn_2012()\
        .should_be_normatives_and_corrections_sn_is_present()


@allure.title('TEST: Проверка наличия Нормативов, Индексов и Поправок у Базы ТСН-2001')
def test_open_database_tsn_2001(switch_to_database_page):
    """"
    Предусловия:
    Пользователь в контексте Базы
    Шаги:
    1. Раскрыть Территориальные сметные нормативы для Москвы ТСН-2001 (МГЭ)
    2. Раскрыть ТСН-2001 (МГЭ)
    Ожидаемое поведение:
    1. Присутствуют Нормативы, Индексы и Поправки
    Постусловия:
    """
    app.normatives_page\
        .should_be_sn_and_tsn_databases_is_present()\
        .open_collection_tsn_2001_mge()\
        .should_be_tsn_2001_and_tsn_13_chapter_is_present()\
        .open_tsn_2001_mge()\
        .should_be_normo_indexes_and_corrections_tsn_is_present()

@allure.title('TEST: Открыть раздел 1 Главы 1 Первоначального издания Базы СН-2012')
def test_open_section_one_sn_base(switch_to_database_page):
    """"
    Предусловия:
    Пользователь в контексте Базы
    Шаги:
    1. Раскрыть сборник стоимостных нормативов для Москвы СН-2012
    2. Раскрыть СН-2012 (в текущих ценах по состоянию на 01.10.2022 года)
    3. Раскрыть Нормативы
    4. Раскрыть Первоначальное издание
    5. Раскрыть главу 1.Здания
    6. Клик на раздел 1 - Земляные работы
    Ожидаемое поведение:
    1.Присутствует Разработка грунта внутри здания в котлованах
    Постусловия:
    """
    app.normatives_page\
        .should_be_sn_and_tsn_databases_is_present()\
        .open_collection_sn_2012()\
        .should_be_current_prices_sn_is_present()\
        .open_current_prices_sn_2012()\
        .should_be_normatives_and_corrections_sn_is_present()\
        .open_normatives()\
        .should_be_normative_code_is_present(TestData.add_num_sn)\
        .open_addition_first_sn()\
        .should_be_chapter_one_sn_is_present()\
        .open_chapter_one_sn()\
        .should_be_section_one_sn()\
        .click_on_section_one_sn()\
        .should_be_material_on_grid_is_present(TestData.work)

@allure.title('TEST: Открыть Техническую часть раздел 1 Главы 1 Первоначального издания Базы СН-2012')
def test_open_techpart_sn_base(switch_to_database_page):
    """"
    Предусловия:
    Пользователь в контексте Базы
    Шаги:
    1. Раскрыть сборник стоимостных нормативов для Москвы СН-2012
    2. Раскрыть СН-2012 (в текущих ценах по состоянию на 01.10.2022 года)
    3. Раскрыть Нормативы
    4. Раскрыть Первоначальное издание
    5. Раскрыть главу 1.Здания
    6. Клик на раздел 1 - Земляные работы
    7. Клик на Техническая часть
    Ожидаемое поведение:
    1.Техчасть открыта
    Постусловия:
    """
    app.normatives_page\
        .should_be_sn_and_tsn_databases_is_present()\
        .open_collection_sn_2012()\
        .should_be_current_prices_sn_is_present()\
        .open_current_prices_sn_2012()\
        .should_be_normatives_and_corrections_sn_is_present()\
        .open_normatives()\
        .should_be_normative_code_is_present(TestData.add_num_sn)\
        .open_addition_first_sn()\
        .should_be_chapter_one_sn_is_present()\
        .open_chapter_one_sn()\
        .should_be_section_one_sn()\
        .click_on_section_one_sn()\
        .should_be_material_on_grid_is_present(TestData.work) \
        .click_on_techpart_button() \
        .should_be_section_one_techpart_sn_is_present()


@allure.title('TEST: Открыть раздел 1 Главы 1 Дополнения 65 Базы ТСН-2001 (МГЭ)')
def test_open_section_one_tsn_base(switch_to_database_page):
    """"
    Предусловия:
    Пользователь в контексте Базы
    Шаги:
    1. Раскрыть Территориальные сметные нормативы для Москвы ТСН-2001 (МГЭ)
    2. Раскрыть ТСН-2001 (МГЭ)
    3. Раскрыть Нормативы
    4. Раскрыть Дополнение 65
    5. Раскрыть Главу 1
    6. Раскрыть Раздел 1
    7. Клик на раздел 1
    Ожидаемое поведение:
    1. Присутствует Аммоний хлористый (нашатырь)
    Постусловия:
    """
    app.normatives_page\
        .should_be_sn_and_tsn_databases_is_present()\
        .open_collection_tsn_2001_mge()\
        .should_be_tsn_2001_and_tsn_13_chapter_is_present()\
        .open_tsn_2001_mge()\
        .should_be_normo_indexes_and_corrections_tsn_is_present()\
        .open_normatives()\
        .should_be_normative_code_is_present(TestData.add_num_tsn)\
        .open_addition_65_tsn()\
        .should_be_chapter_one_is_present()\
        .open_chapter_one_tsn()\
        .should_be_section_one()\
        .click_on_section_one()\
        .should_be_material_on_grid_is_present(TestData.material)


@allure.title('TEST: Открыть Техническую часть Раздела 1 Главы 1 Дополнения 65 Базы ТСН-2001 (МГЭ)')
def test_open_techpart_tsn_base(switch_to_database_page):
    """"
    Предусловия:
    Пользователь в контексте Базы
    Шаги:
    1. Раскрыть Территориальные сметные нормативы для Москвы ТСН-2001 (МГЭ)
    2. Раскрыть ТСН-2001 (МГЭ)
    3. Раскрыть Нормативы
    4. Раскрыть Дополнение 65
    5. Раскрыть Главу 1
    6. Раскрыть Раздел 1
    7. Клик на раздел 1
    8. Клик на Техническую часть
    Ожидаемое поведение:
    1. Техчасть открыта
    Постусловия:
    """
    app.normatives_page\
        .should_be_sn_and_tsn_databases_is_present()\
        .open_collection_tsn_2001_mge()\
        .should_be_tsn_2001_and_tsn_13_chapter_is_present()\
        .open_tsn_2001_mge()\
        .should_be_normo_indexes_and_corrections_tsn_is_present()\
        .open_normatives()\
        .should_be_normative_code_is_present(TestData.add_num_tsn)\
        .open_addition_65_tsn()\
        .should_be_chapter_one_is_present()\
        .open_chapter_one_tsn()\
        .should_be_section_one()\
        .click_on_section_one()\
        .click_on_techpart_button()\
        .should_be_section_one_techpart_tsn_is_present()

@allure.title('TEST: Открыть Индексы 2022 ноябрь Базы ТСН-2001 (МГЭ)')
def test_open_indexes_tsn_base(switch_to_database_page):
    """"
    Предусловия:
    Пользователь в контексте Базы
    Шаги:
    1. Раскрыть Территориальные сметные нормативы для Москвы ТСН-2001 (МГЭ)
    2. Раскрыть ТСН-2001 (МГЭ)
    3. Раскрыть Индексы
    4. Раскрыть год 2022
    5. Раскрыть месяц ноябрь
    7. Клик на ноябрь
    Ожидаемое поведение:
    1. Таблица с индексами открыта
    Постусловия:
    """
    app.normatives_page\
        .should_be_sn_and_tsn_databases_is_present()\
        .open_collection_tsn_2001_mge()\
        .should_be_tsn_2001_and_tsn_13_chapter_is_present()\
        .open_tsn_2001_mge()\
        .should_be_normo_indexes_and_corrections_tsn_is_present()\
        .open_indexes()\
        .should_be_indexes_is_present()\
        .open_year_2022()\
        .should_be_indexes_month_is_present(TestData.ind_month)\
        .click_on_month(TestData.ind_month)\
        .should_be_indexes_grid_is_present()


@allure.title('TEST: Открыть Поправки для ТСН-2001 от 15.10.2022 г. доп 66')
def test_open_correction_tsn_base(switch_to_database_page):
    """"
    Предусловия:
    Пользователь в контексте Базы
    Шаги:
    1. Раскрыть Территориальные сметные нормативы для Москвы ТСН-2001 (МГЭ)
    2. Раскрыть ТСН-2001 (МГЭ)
    3. Раскрыть Поправки
    4. Клик на Поправки для ТСН-2001 от 15.10.2022 г. доп 66
    Ожидаемое поведение:
    1. Открыт грид с поправками
    Постусловия:
    """
    app.normatives_page\
        .should_be_sn_and_tsn_databases_is_present()\
        .open_collection_tsn_2001_mge()\
        .should_be_tsn_2001_and_tsn_13_chapter_is_present()\
        .open_tsn_2001_mge()\
        .should_be_normo_indexes_and_corrections_tsn_is_present()\
        .open_corrections()\
        .should_be_corrections_is_present(TestData.cor_name)\
        .click_on_correction_name(TestData.cor_name)\
        .should_be_corrections_code_is_present(TestData.cor_code_tsn)


@allure.title('TEST: Открыть Поправки для СН-2012 (в ценах на 01.10.2022 года)')
def test_open_correction_sn_base(switch_to_database_page):
    """"
    Предусловия:
    Пользователь в контексте Базы
    Шаги:
    1. Раскрыть сборник стоимостных нормативов для Москвы СН-2012
    2. Раскрыть СН-2012 (в текущих ценах по состоянию на 01.10.2022 года)
    3. Раскрыть Поправки
    4. Клик на Поправки для СН-2012 (в ценах на 01.10.2022 года)
    Ожидаемое поведение:
    1. Открыт грид с поправками
    Постусловия:
    """
    app.normatives_page\
        .should_be_sn_and_tsn_databases_is_present()\
        .open_collection_sn_2012()\
        .should_be_current_prices_sn_is_present()\
        .open_current_prices_sn_2012()\
        .should_be_normatives_and_corrections_sn_is_present()\
        .open_corrections() \
        .should_be_corrections_is_present(TestData.cor_name_sn) \
        .click_on_correction_name(TestData.cor_name_sn) \
        .should_be_corrections_code_is_present(TestData.cor_code_sn)