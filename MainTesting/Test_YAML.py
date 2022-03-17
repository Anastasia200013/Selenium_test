import yaml
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from yaml.loader import SafeLoader
from MainTesting.conftest import driver_init


# Функция ожидания элементов
def wait_of_element_located(selector, driver_init):
    element = WebDriverWait(driver_init, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, selector)
        )
    )
    return element


# Функция проверки зачения на соответсвие регулярному выражению
def regex(f_element, reg_text, driver_init):
    search_element = WebDriverWait(driver_init, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, f_element)
        )
    )
    element = search_element.text
    check_test = re.fullmatch(reg_text, element)
    print('YES' if check_test else 'NO')


# Тест
def test_add_jacket_to_the_shopcart(driver_init, auth_user, perechod):
    with open('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\TestsYML\\Test.yml', encoding='utf-8') as f:
        # Загрузка YAML данных из файла
        read_data_test = dict(yaml.load(f, Loader=SafeLoader))
    # file_name = str(read_data_test['TestDescription']['FileSelectors'])
    test_reg_ab = str(read_data_test['TestDescription']['Tests'][0]['Exp'])
    test_reg_fio = str(read_data_test['TestDescription']['Tests'][1]['Exp'])
    test_reg_address = str(read_data_test['TestDescription']['Tests'][2]['Exp'])
    # test_reg_ow = str(read_data_test['TestDescription']['TestInfoOwner'])
    print(test_reg_ab, ';', test_reg_fio, ';', test_reg_address)

    with open('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSlect\\SearchSelectors.yml', encoding='utf-8') as h:
        # Загрузка YAML данных из файла
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
