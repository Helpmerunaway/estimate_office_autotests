import allure
import pytest
from estimate_tests.utils.date_and_time import today_date
from estimate_tests.ui.application_manager import app
from estimate_tests.data.data import TestData



"""

Проверка работы контекста Сметы

"""


@pytest.mark.objects
@allure.title('TEST: Проверка раскрытия дерева Мои Сметы')
def test_open_my_estimates(switch_to_objects_page):
    """
        Предусловия:
        Пользователь находится на странице objects
        Шаги:
        1. Раскрыть иерархию "Мои сметы"
        Ожидаемый результат:
        Древо "Мои сметы" раскрыто
        Постусловия:
        Разлогин
        """
    app.objects_page\
        .open_the_hierarchy_my_estimates()


@pytest.mark.objects
@allure.title('TEST: Проверка раскрытия дерева Мои Сметы')
def test_create_new_folder(switch_to_objects_page):
    """
        Предусловия:
        Пользователь находится на странице objects
        Шаги:
        1. Создать папку
        Ожидаемый результат:
        Папка создана
        Постусловия:
        Удаление папки
        """
    app.objects_page \
        .open_the_hierarchy_my_estimates()\
        .create_new_folder()\
        .should_be_new_folder_present()


@pytest.mark.objects
@allure.title('TEST: Проверка перехода по вкладкам риббона')
def test_ribbon_buttons(switch_to_objects_page):
    """
        Предусловия:
        Пользователь находится на странице objects
        Шаги:
        1. Переход на вкладку Вставка
        2. Переход на вкладку Объемы
        3. Переход на вкладку Вид
        4. Переход на вкладку Операции
        5. Переход на вкладку Отчет
        6. Переход на вкладку Главная
        Ожидаемый результат:
        На вкладках присутствуют кнопки риббона
        Постусловия:
        Разлогин
        """
    app.objects_page.click_on_ribbon_paste_tab()\
        .click_on_ribbon_volumes_tab()\
        .click_on_ribbon_view_tab()\
        .click_on_ribbon_operation_tab()\
        .click_on_ribbon_report_tab()\
        .click_on_ribbon_main_tab()


@allure.title('TEST: Копировать вставить папку')
def test_copy_paste_folder(switch_to_objects_page):
    """
        Предусловия:
        Пользователь находится на странице objects
        Создана папка
        Шаги:
        1. Скопировать папку
        2. Вставить папку
        Ожидаемый результат:
        Алерт
        Постусловия:
        Удалить папку
        """
    app.objects_page \
        .open_the_hierarchy_my_estimates() \
        .create_new_folder()\
        .copy_and_paste_folder()


@allure.title('TEST: Проверка создания сметы СН')
def test_create_estimate_sn_2012(switch_to_objects_page):
    """"
    Предусловия:
    Пользователь находится на странице objects
    Создана папка и смета СН
    Шаги:
    1. Заполнить поле Наименование сметы
    2. Заполнить поле Наименование объекта
    3. Заполнить поле Номер/Шифр сметы
    4. Выбор базы из дропдауна
    5. Выбор дополнения из дропдауна
    6. Клик на кнопку Редактировать смету
    Ожидаемое поведение:
    В заголовке присутствует название сметы
    Постусловия:
    Удалить тестовые данные
    """
    app.objects_page \
        .open_the_hierarchy_my_estimates() \
        .create_new_folder()\
        .click_new_estimate_button()\
        .fill_field_estimate_name(TestData.sn_name)\
        .fill_field_object_name(TestData.obj_name)\
        .fill_field_number_of_estimate(TestData.estimate_num) \
        .choose_database_name_sn_from_dropdown() \
        .choose_addition_from_dropdown()\
        .click_on_edit_estimate_button()\
        .should_be_estimate_name_present(TestData.sn_name)\
        .back_to_objects_page()


@allure.title('TEST: Проверка создания сметы ТСН')
def test_create_estimate_tsn_2001_mge(switch_to_objects_page):
    """"
    Предусловия:
    Пользователь находится на странице objects
    Создана папка и смета ТСН
    Шаги:
    1. Заполнить поле Наименование сметы
    2. Заполнить поле Наименование объекта
    3. Заполнить поле Номер/Шифр сметы
    4. Выбор базы из дропдауна
    5. Выбор дополнения из дропдауна
    6. Клик на кнопку Редактировать смету
    Ожидаемое поведение:
    В заголовке присутствует название сметы
    Постусловия:
    Удалить тестовые данные
    """
    app.objects_page \
        .open_the_hierarchy_my_estimates() \
        .create_new_folder()\
        .click_new_estimate_button()\
        .fill_field_estimate_name(TestData.tsn_name)\
        .fill_field_object_name(TestData.obj_name)\
        .fill_field_number_of_estimate(TestData.estimate_num) \
        .choose_database_name_tsn_from_dropdown() \
        .choose_addition_tsn_65_from_dropdown()\
        .choose_indexes_tsn_from_dropdown()\
        .choose_tsn_chapter_13_from_dropdown()\
        .choose_indexes_chapter_13_from_dropdawn() \
        .click_on_edit_estimate_button() \
        .should_be_estimate_name_present(TestData.tsn_name) \
        .back_to_objects_page()


@allure.title('TEST: Проверка удаления сметы')
def test_delete_estimate(switch_to_objects_page):
    """"
    Предусловия:
    Пользователь находится на странице objects
    Шаги:
    1. Создать обьект сметы
    2. Удалить обьект сметы
    Ожидаемое поведение:
    В заголовке присутствует название сметы
    Постусловия:
    Удалить тестовые данные
    """
    app.objects_page \
        .open_the_hierarchy_my_estimates() \
        .click_new_estimate_button()\
        .click_delete_button()\
        .should_be_estimate_in_trashbox()


@allure.title('TEST: Проверка очистки корзины')
def test_empty_trashbox(switch_to_objects_page):
    """"
        Предусловия:
        Пользователь находится на странице objects
        Шаги:
        1. Создать обьект сметы
        2. Удалить обьект сметы
        3. Очистить корзину
        Ожидаемое поведение:
        Корзина пуста
        Постусловия:
        Удалить тестовые данные
        """
    app.objects_page \
        .open_the_hierarchy_my_estimates() \
        .click_new_estimate_button() \
        .click_delete_button() \
        .click_on_empty_trash_button()\
        .should_be_trashbox_is_empty()