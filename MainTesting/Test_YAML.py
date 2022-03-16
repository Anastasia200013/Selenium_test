import pytest
import yaml
import re
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from yaml.loader import SafeLoader
from selenium import webdriver
from MainTesting.conftest import driver_init
from selenium.webdriver.common.keys import Keys


# Функция ожидания элементов
def wait_of_element_located(selector, driver_init):
    element = WebDriverWait(driver_init, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, selector)
        )
    )
    return element


# Функция проверки зачения на соответсвие регулярному выражению
def regex(f_lement, reg_text, driver_init):
    search_element = WebDriverWait(driver_init, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, f_lement)
        )
    )
    element = search_element.text
    check_test = re.fullmatch(reg_text, element)
    print('YES' if check_test else 'NO')


# Вынесем аутентификацию юзера в отдельную функцию
def auth_user(user_name, password, driver_init):
    # Поиск и ожидание элементов и присваивание к переменным.
    input_username = wait_of_element_located(selector='#input_login_01', driver_init=driver_init)
    input_password = wait_of_element_located(selector='#input_password_01', driver_init=driver_init)
    button_enter = wait_of_element_located(selector='#btn_login_accept_01.btn.btn-primary.btn-modal',
                                           driver_init=driver_init)
    # Действия с формами
    time.sleep(2)
    input_username.send_keys(user_name)
    time.sleep(2)
    input_password.send_keys(password)
    time.sleep(2)
    button_enter.send_keys(Keys.RETURN)
    time.sleep(4)


# переход на нужную старницу
def perechod(driver_init):
    search_abonent = wait_of_element_located(selector='div#navbar_collapse_01 ul.nav.navbar-nav:nth-child(1) '
                                                      'li:nth-child(2)>a', driver_init=driver_init)
    search_abonent.send_keys(Keys.RETURN)
    time.sleep(6)


# Тест
def test_add_jacket_to_the_shopcart(driver_init):
    # Аутентификация пользователя
    with open('D:\Fixtures\Fixture.yml', encoding='utf-8') as fd:
        # Load YAML data from the file
        read_options = dict(yaml.load(fd, Loader=SafeLoader))
    login_user = str(read_options['TestUsers'][1]['Login'])
    password_user = str(read_options['TestUsers'][1]['Password'])

    auth_user(login_user, password_user, driver_init=driver_init)

    perechod(driver_init=driver_init)

    with open('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\TestsYML\\Test.yml', encoding='utf-8') as f:
        # Load YAML data from the file
        read_data_test = dict(yaml.load(f, Loader=SafeLoader))
    # file_name = str(read_data_test['TestDescription']['FileSelectors'])
    test_reg_ab = str(read_data_test['TestDescription']['Tests'][0]['Exp'])
    test_reg_fio = str(read_data_test['TestDescription']['Tests'][1]['Exp'])
    test_reg_address = str(read_data_test['TestDescription']['Tests'][2]['Exp'])
    # test_reg_ow = str(read_data_test['TestDescription']['TestInfoOwner'])
    print(test_reg_ab, ';', test_reg_fio, ';', test_reg_address)

    with open('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSlect\\SearchSelectors.yml', encoding='utf-8') as h:
        # Load YAML data from the file
        read_data_slcrt = dict(yaml.load(h, Loader=SafeLoader))

    selector_ab = str(read_data_slcrt['Selectors']['Locations'][0]['Location'])
    selector_fio = str(read_data_slcrt['Selectors']['Locations'][1]['Location'])
    selector_address = str(read_data_slcrt['Selectors']['Locations'][2]['Location'])
    # selector_ow = str(read_data_slcrt['Selectors']['StrOwnerid'])
    print(selector_ab, ';', selector_fio, ';', selector_address)

    regex(selector_ab, test_reg_ab, driver_init=driver_init)
    regex(selector_fio, test_reg_fio, driver_init=driver_init)
    regex(selector_address, test_reg_address, driver_init=driver_init)
    # regex(selector_ow, test_reg_ow, driver_init=driver_init)


if __name__ == '__main__':
    test_add_jacket_to_the_shopcart(driver_init=driver_init)
