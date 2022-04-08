import yaml
import re
import time
from selenium.webdriver.common.keys import Keys
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
def regex(f_element, reg_text, driver):
    search_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, f_element)
        )
    )
    element = search_element.text
    check_test = re.fullmatch(reg_text, element)
    print('YES' if check_test else 'NO')


def read_file_to_dictionary(file_name):
    with open(file_name, 'r', encoding='utf-8') as h:
        # Загрузка YAML данных из файла
        read_data_slcrt = dict(yaml.load(h, Loader=SafeLoader))
        return read_data_slcrt


def write_dictionary_to_file(file_name, dictionary):
    with open(file_name, 'w') as f:
        yaml.dump(dictionary, f)


def go_to_pages(selector, driver_init_admin):
    search_abonent = wait_of_element_located_fix(selector=selector, driver=driver_init_admin)
    search_abonent.send_keys(Keys.RETURN)
    time.sleep(6)


def generate_dict_selectors(d):
    key = str(list(d.keys())[0])
    new_d = {"Selectors": {
        "FileTest": "",
        "Type": key,
        "Locations": [{
            "FieldName": str(k),
            "Location": ""}
            for k in d[key].keys()]
        }
    }
    return new_d


def generate_test_script(object_class, path):
    fields = list(object_class.__dict__["__annotations__"].keys())
    # result = "\n".join(["import time", "from pathlib import Path", "from selenium.webdriver.common.keys import Keys",
    #                     "from OnBeforeTest.conftest import driver_init_user",
    #                     "from inenv.Lib.Utility import read_file_to_dictionary, wait_of_element_located_fix, regex"])
    result = "\n"
    for i, field in enumerate(fields):
        result += f"def test_regex_{field}(driver_init_user):\n"
        result += f"    file_name = str(read_file_to_dictionary(path_searchselect)['Selectors']['FileTest'])\n"
        result += f"    selector_{field} = str(read_file_to_dictionary(path_searchselect)['Selectors']['Locations'][{i}]['Location'])\n"
        result += f"    test_reg_{field} = str(read_file_to_dictionary(file_name)['TestDescription']['Tests'][{i}]['Exp'])\n"
        result += f"    regex(selector_{field}, test_reg_{field}, driver=driver_init_user)\n\n"

    with open(path, "a") as f:
        f.write(result)
