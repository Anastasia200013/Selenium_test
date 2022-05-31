import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inenv.Lib.Selector import Selectors, Location
from inenv.Lib.Case import TestDescription, Test
import pathlib
from pathlib import Path

class RegexWrapper:
    @staticmethod
    def get_test_args(path_searchselect, field_test_name):
        selector = Selectors.load(path_searchselect)
        file_name = selector.file_test
        path_test = Path(pathlib.Path.home(), file_name)
        location = Location.find_by_field_name(selector.locations, field_test_name).location
        suite = TestDescription.load(path_test)
        case = Test.find_by_statement(suite.tests, f"FOR {selector.type}.{field_test_name}")
        reg_expr = case.exp
       # if case.type == 'Regex.fullMatch':
        return location, reg_expr
       # else:
          #  print("В указанной коллекции нет тестов на регулярные выражения!")
        print('faafaf', path_searchselect)

    @staticmethod
    def regex(f_element, reg_text, driver):
        search_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, f_element)
            )
        )
        element = search_element.text
        check_test = re.fullmatch(reg_text, element)
        print('YES' if check_test else 'NO')

    @staticmethod
    def page(selector, driver):
        search_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, selector)
            )
        )
        element = search_element.click
        print('YES' if element else 'NO')

    @staticmethod
    def generate_test_regex_script(object_class, test_class, path):
        fields = object_class.__dict__["__annotations__"]
        result = f"from inenv.Lib.RegexWrapper import RegexWrapper\n"
        result += f"from OnBeforeTest.conftest import driver_init_{test_class}\n"
        result += f"from inenv.Lib.Utility import Utility\n\n"
        result += f"\nclass {test_class}(RegexWrapper):\n"
        result += f"    class_test_name = \"{str(object_class.__name__)}\"\n"
        result += "    path_select = Path(pathlib.Path.home(), 'PycharmProjects', 'selenium-test', 'SearchSelect', '*.yml')\n\n"

        for k, v in fields.items():
            if type(v) == type(str.__class__):
                result += f"    @staticmethod\n"
                result += f"    def test_regex_{k}(driver_init_user):\n"
                result += f"        location, reg_expr = {test_class}.get_test_args({test_class}.path_searchselect, \"{k}\")\n"
                result += f"        RegexWrapper.regex(location, reg_expr, driver=driver_init_user)\n\n"

        with open(path, "w") as f:
            f.write(result)
