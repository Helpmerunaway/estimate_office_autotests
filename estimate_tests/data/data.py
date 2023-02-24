from dataclasses import dataclass
from enum import Enum
from typing import Tuple

from estimate_tests.utils.date_and_time import today_date


# DEV
class Users():

    @dataclass
    class AdminDev:
        login: str = f'{login}'
        password: str = f'{password}'
        email: str = f"{email}"


    class EmptyUserDev:
        login: str = f'{login}'
        password: str = f'{password}'
        email: str = f"{email}"


    class NoLicenceDev:
        login: str = f'{login}'
        password: str = f'{password}'
        email: str = f"{email}"


    class Autotest:
        login: str = f'{login}'
        password: str = f'{password}'
        email: str = f"{email}"


    class UrLico:
        login: str = f'{login}'
        password: str = f'{password}'
        email: str = f"{email}"

    # PREVIEW


    @dataclass
    class AdminUserPrev:
        login: str = f'{login}'
        password: str = f'{password}'
        email: str = f"{email}"
        fake_login: str = "fake_user_login"



    @dataclass
    class NoLicenseUserPrev:
        login: str = f'{login}'
        password: str = f'{password}'
        email: str = f"{email}"



    @dataclass
    class NewUserPrev:
        login: str = f'{login}'
        password: str = f'{password}'
        email: str = f"{email}"


class TestData:
    sn_name = 'SN_2012_' + today_date
    tsn_name = 'TSN_2001' + today_date
    obj_name = '111'
    estimate_num = "1234"
    just_num = "3.15-1-1"
    resource_one = '3971790000'
    resource_disk = '1.7-3-1'
    pricing_value = '100'
    keyword = 'кирпич'
    pricing_code = '6.53-16-2'
    text_pricing = 'Облицовка стен гранитными плитами полированными толщиной 40 мм при числе плит в 1 м2 до 2'
    mat_num = '1 1 1 1'
    mat_text = "Материал по прайсу"
    equip_num = '2 2 2 2'
    equip_text = 'Оборудование по прайсу'
    mach_num = '3 3 3 3'
    mach_text = 'Машина по прайсу'
    comment_text = 'Первый'
    add_num_tsn = 'Дополнение 65'
    add_num_sn = 'Первоначальное издание'
    material = 'Аммоний хлористый (нашатырь)'
    work = 'Разработка грунта внутри здания в котлованах'
    ind_month = 'ноябрь'
    mp = '12,14'
    cor_name = 'Поправки для ТСН-2001 от 15.10.2022 г. доп 66'
    cor_name_sn = 'Поправки для СН-2012 (в ценах на 01.10.2022 года)'
    cor_code_tsn = 'О.П. сб.12 т.6.2 п. 1.1'
    cor_code_sn = 'СН-2012 О.П. п.22'
    empty_req = ''