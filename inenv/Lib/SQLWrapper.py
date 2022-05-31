from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pathlib
from pathlib import Path
from inenv.Lib.Selector import Selectors, Location
from inenv.Lib.Case import TestDescription, Test
from inenv.Lib.Utility import Utility


class SQLWrapper:
    path_fix = '\\selenium-test\\Fixture.yml'

    @staticmethod
    def get_test_components(path_searchselect, field_test_name):
        selector = Selectors.load(path_searchselect)
        file_name = selector.file_test
        path_test = Path(pathlib.Path.home(), file_name)
        location = Location.find_by_field_name(selector.locations, field_test_name).location
        suite = TestDescription.load(path_test)
        case = Test.find_by_statement(suite.tests, f"FOR {selector.type}.{field_test_name}")
        request_sql = case.exp
        #if case.type == 'SQL.Request':
        return location, request_sql
        #else:
         #   print("В указанной коллекции нет тестов с запросом к БД!")
        print('faafaf', suite)

    @staticmethod
    def select_request(request, path_bd):
        con = Utility.connect_bd(path_bd)
        cur = con.cursor()
        cur.execute(request) # "Select count(*) from BALANCESLIST"
        result = str(cur.fetchall()[0][0])
        print(result)
        return result

    @staticmethod
    def check_request(f_element, request, driver):
        search_element = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, f_element)
            )
        )
        path_fix = Path(pathlib.Path.home(), 'PycharmProjects', 'selenium-test', 'Fixture.yml')
        element = str(search_element.text)
        path = (Utility.read_file_to_dictionary(path_fix)['TestConnection']['BD'])
        request_result = str(SQLWrapper.select_request(request, path))
        print('aaaaa', element)
        print('YES' if element == request_result else 'NO')
        print('ffsff', request_result)


    @staticmethod
    def check_list(f_element, request, driver):
        search_elements = WebDriverWait(driver, 20).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, f_element)
            )
        )
        elements_count = len(search_elements)
        request_result = int(SQLWrapper.select_request(request))
        print('YES' if elements_count == request_result else 'NO')
        print('aaa', elements_count)


    @staticmethod
    def generate_test_request_script(object_class, test_class, path):
        fields = object_class.__dict__["__annotations__"]
        result = f"from inenv.Lib.SQLWrapper import SQLWrapper\n"
        result += f"from OnBeforeTest.conftest import driver_init_{test_class}\n"
        result += f"from inenv.Lib.Utility import Utility\n\n"
        result += f"\nclass {test_class}(SQLWrapper):\n"
        result += f"    class_test_name = \"{str(object_class.__name__)}\"\n"
        result += "    path_select = Path(pathlib.Path.home(), 'PycharmProjects', 'selenium-test', 'SearchSelect', '*.yml')\n\n"

        for k, v in fields.items():
            if type(v) == type(int.__class__):
                result += f"    @staticmethod\n"
                result += f"    def test_request_{k}(driver_init_user):\n"
                result += f"        location, request_sql = {test_class}.get_test_components({test_class}.path_searchselect, \"{k}\")\n"
                result += f"        SQLWrapper.check_request(location, request_sql, driver=driver_init_user)\n\n"

        with open(path, "w") as f:
            f.write(result)



