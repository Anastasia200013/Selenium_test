import yaml
import re
import  time
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from yaml.loader import SafeLoader


# Функция ожидания элементов
def wait_of_element_located_fix(selector, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, selector)
        )
    )
    return element


# Функция проверки зачения на соответсвие регулярному выражению
def regex(f_element, reg_text, driver_init_admin):
    search_element = WebDriverWait(driver_init_admin, 20).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, f_element)
        )
    )
    element = search_element.text
    check_test = re.fullmatch(reg_text, element)
    print('YES' if check_test else 'NO')


def read_file_to_dictionary(file_name):
    with open(file_name, encoding='utf-8') as h:
        # Загрузка YAML данных из файла
        read_data_slcrt = dict(yaml.load(h, Loader=SafeLoader))
        return read_data_slcrt


'''def go_to_pages(selector, driver_init_admin):
    search_abonent = wait_of_element_located_fix(selector=selector, driver_init_admin=driver_init_admin)
    search_abonent.send_keys(Keys.RETURN)
    time.sleep(6)'''