import allure
import pytest

from estimate_tests.utils.date_and_time import today_date
from estimate_tests.ui.application_manager import app
from estimate_tests.data.data import TestData

"""

Проверка работы контекста Открытые

"""

@allure.title('TEST: Вставка расценки')
def test_paste_addprice(create_estimate_tsn):
    """"
    Предусловия:
    Пользователь находится на странице objects
    Создана папка и смета ТСН
    Шаги:
    1. Добавить расценку
    Ожидаемое поведение:
    Расценка добавлена
    Постусловия:
    Удалить тестовые данные
    """
    app.estimates_page\
        .click_on_pastetab_button()\
        .click_on_button_addprice()\
        .should_be_pricing_is_present()


@allure.title('TEST: Удаление расценки')
def test_delete_addprice(create_estimate_tsn):
    """"
    Предусловия:
    Пользователь находится на странице objects
    Создана папка и смета ТСН
    Шаги:
    1. Добавить расценку
    2. Удалить расценку
    Ожидаемое поведение:
    Расценка удалена
    Постусловия:
    Удалить тестовые данные
    """
    app.estimates_page \
        .click_on_pastetab_button() \
        .click_on_button_addprice()\
        .click_on_delete_button()


@allure.title('TEST: Перевызов обоснования')
def test_recall_justification(create_estimate_tsn):
    """"
        Предусловия:
        Пользователь находится на странице objects
        Создана папка и смета ТСН
        Шаги:
        1. Добавить расценку
        2. Ввести обоснование
        3. Перевызвать обоснование
        Ожидаемое поведение:
        Обоснование перевызвано
        Постусловия:
        Удалить тестовые данные
        """
    app.estimates_page\
        .click_on_pastetab_button()\
        .click_on_button_addprice()\
        .click_on_pressmark_and_recall(TestData.just_num)\
        .should_be_correct_text_present()


@allure.title('TEST: Разукрупнение группового ресурса')
def test_unbundling_a_resource(create_estimate_tsn):
    """"
            Предусловия:
            Пользователь находится на странице objects
            Создана папка и смета ТСН
            Шаги:
            1. Добавить расценку
            2. Ввести обоснование
            3. Перевызвать обоснование
            4. Разукрупнить групповой ресурс
            Ожидаемое поведение:
            Ресурс разукрупнен
            Постусловия:
            Удалить тестовые данные
            """
    app.estimates_page \
        .click_on_pastetab_button() \
        .click_on_button_addprice() \
        .click_on_pressmark_and_recall(TestData.just_num)\
        .unbundling_a_resource(TestData.resource_one)\
        .choose_resource_from_modal(TestData.resource_disk) \
        .should_be_unbundled_resource_is_present(TestData.resource_disk)


@pytest.mark.skip(reason='unicode error')
@allure.title('TEST: Проверка пересчета стоимости расценки')
def test_cost_of_pricing(create_estimate_tsn):
    """"
            Предусловия:
            Пользователь находится на странице objects
            Создана папка и смета ТСН
            Шаги:
            1. Добавить расценку
            2. Перевызвать обоснование
            3. Итоги по смете - 0
            4. Проставить объем
            Ожидаемое поведение:
            Итоговая стоимость сметы изменилась
            Постусловия:
            Удалить тестовые данные
            """
    app.estimates_page \
        .click_on_pastetab_button() \
        .click_on_button_addprice() \
        .click_on_pressmark_and_recall(TestData.just_num)\
        .should_be_zero_estimate_cost()\
        .should_be_correct_text_present()\
        .enter_value_of_pricing(TestData.pricing_value)\
        .should_be_correct_value_of_pricing(TestData.pricing_value)\
        .should_be_correct_estimate_cost()


@allure.title('TEST: Копировать вставить норматив из поиска')
def test_copy_and_past_normative_from_search(create_estimate_tsn):
    """"
            Предусловия:
            Пользователь находится на странице objects
            Создана папка и смета ТСН
            Шаги:
            1. Клик на кнопку Поиск
            2. Проверка открылось ли окно поиска
            3. Поиск по ключевому слову
            4. Скопировать норматив
            5. Вставить норматив
            Ожидаемое поведение:
            Норматив вставлен
            Постусловия:
            Удалить тестовые данные
            """
    app.estimates_page\
        .click_on_search_button()\
        .should_be_search_window_is_present()\
        .click_and_type_search(TestData.keyword)\
        .copy_normative()\
        .close_search_window()\
        .context_click_on_chapter_one()\
        .paste_normative_into_estimate()\
        .should_be_correct_pricing_is_present(TestData.pricing_code)


@allure.title('TEST: Копировать вставить расценку')
def test_copy_and_paste_pricing(create_estimate_tsn):
    """"
            Предусловия:
            Пользователь находится на странице objects
            Создана папка и смета ТСН
            Шаги:
            1. Добавить расценку
            2. Перевызвать
            3. Скопировать
            4. Вставить
            Ожидаемое поведение:
            Расценка вставлена
            Постусловия:
            Удалить тестовые данные
            """
    app.estimates_page \
        .click_on_pastetab_button() \
        .click_on_button_addprice() \
        .click_on_pressmark_and_recall(TestData.just_num)\
        .should_be_correct_text_present()\
        .click_on_maintab_copy_button()\
        .click_on_maintab_paste_button()\
        .should_be_pasted_pricing_is_present(TestData.text_pricing)


@allure.title('TEST: Вставить раздел')
def test_paste_new_section(create_estimate_tsn):
    """"
            Предусловия:
            Пользователь находится на странице objects
            Создана папка и смета ТСН
            Шаги:
            1. Добавить раздел
            Ожидаемое поведение:
            Раздел добавлен
            Постусловия:
            Удалить тестовые данные
            """
    app.estimates_page \
        .click_on_pastetab_button() \
        .click_on_add_new_section_button()\
        .should_be_new_section_is_present()


@allure.title('TEST: Добавить материал')
def test_add_material(create_estimate_tsn):
    """"
            Предусловия:
            Пользователь находится на странице objects
            Создана папка и смета ТСН
            Шаги:
            1. Добавить материал
            2. Заполнить наименование и обоснование
            Ожидаемое поведение:
            Материал добавлен
            Постусловия:
            Удалить тестовые данные
            """
    app.estimates_page \
        .click_on_pastetab_button() \
        .click_on_add_material_button() \
        .fill_fields_justification_and_name(TestData.mat_num, TestData.mat_text)\
        .should_be_line_is_present(TestData.mat_text)


@allure.title('TEST: Добавить оборудование')
def test_add_equipment(create_estimate_tsn):
    """"
            Предусловия:
            Пользователь находится на странице objects
            Создана папка и смета ТСН
            Шаги:
            1. Добавить оборудование
            2. Заполнить наименование и обозначение
            Ожидаемое поведение:
            Оборудование добавлено
            Постусловия:
            Удалить тестовые данные
            """
    app.estimates_page \
        .click_on_pastetab_button() \
        .click_on_add_equipment_button() \
        .fill_fields_justification_and_name(TestData.equip_num, TestData.equip_text)\
        .should_be_line_is_present(TestData.equip_text)


@allure.title('TEST: Добавить машину')
def test_add_machine(create_estimate_tsn):
    """"
            Предусловия:
            Пользователь находится на странице objects
            Создана папка и смета ТСН
            Шаги:
            1. Добавить машину
            2. Заполнить наименование и обозначение
            Ожидаемое поведение:
            Машина добавлена
            Постусловия:
            Удалить тестовые данные
            """
    app.estimates_page \
        .click_on_pastetab_button()\
        .click_on_add_machine_button() \
        .fill_fields_justification_and_name(TestData.mach_num, TestData.mach_text) \
        .should_be_line_is_present(TestData.mach_text)


@allure.title('TEST: Добавить комментарий')
def test_add_comment(create_estimate_tsn):
    """"
            Предусловия:
            Пользователь находится на странице objects
            Создана папка и смета ТСН
            Шаги:
            1. Добавить комментарий
            2. Переименовать комментарий
            Ожидаемое поведение:
            Комментарий добавлен
            Постусловия:
            Удалить тестовые данные
            """
    app.estimates_page \
        .click_on_pastetab_button()\
        .click_on_add_comment_button()\
        .rename_comment(TestData.comment_text)\
        .should_be_comment_is_present(TestData.comment_text)


@allure.title('TEST: Переход к нормативу')
def test_jump_to_normo(create_estimate_tsn):
    """"
            Предусловия:
            Пользователь находится на странице objects
            Создана папка и смета ТСН
            Шаги:
            1. Добавить расценку
            2. Перевызвать обоснование
            3. Контекстный клик на расценке
            4. Перейти к нормативу
            Ожидаемое поведение:
            В гриде присутствует обоснование
            Постусловия:
            Удалить тестовые данные
            """
    app.estimates_page \
        .click_on_pastetab_button() \
        .click_on_button_addprice() \
        .click_on_pressmark_and_recall(TestData.just_num)\
        .should_be_correct_text_present()\
        .context_click_on_pricing(TestData.just_num)\
        .click_jump_to_normo_from_context_menu()\
        .should_be_normative_on_grid()

@allure.title('TEST: Открыть техчасть')
def test_open_techpart(create_estimate_tsn):
    """"
            Предусловия:
            Пользователь находится на странице objects
            Создана папка и смета ТСН
            Шаги:
            1. Добавить расценку
            2. Перевызвать обоснование
            3. Контекстный клик на расценке
            4. Открыть техчасть
            Ожидаемое поведение:
            Открыта техчасть
            Постусловия:
            Удалить тестовые данные
            """
    app.estimates_page \
        .click_on_pastetab_button() \
        .click_on_button_addprice() \
        .click_on_pressmark_and_recall(TestData.just_num)\
        .should_be_correct_text_present() \
        .context_click_on_pricing(TestData.just_num)\
        .click_open_tech_doc_from_context_menu() \
        .should_be_correct_tech_doc_is_open()


@pytest.mark.xfail(reason='not done')
@allure.title('TEST: Индексы пересчета')
def test_conversion_index(create_estimate_tsn):
    pass