from inenv.Lib.RegexWrapper import RegexWrapper
import pathlib
from pathlib import Path
from OnBeforeTest.conftest import driver_init_user
from inenv.Lib.Utility import Utility


class TestRegexAbonent(RegexWrapper):
    class_test_name = "Abonent"
    #path_searchselect = '\\selenium-test\\SearchSelect\\SelectorsAbonent.yml'
    path_select = Path(pathlib.Path.home(), 'PycharmProjects', 'selenium-test', 'SearchSelect', 'SelectorsAbonent.yml')

    @staticmethod
    def test_regex_accountcd(driver_init_user):
        location, reg_expr = TestRegexAbonent.get_test_args(TestRegexAbonent.path_select, "accountcd")
        RegexWrapper.regex(location, reg_expr, driver=driver_init_user)
       # print(path_select)

    @staticmethod
    def test_regex_fio(driver_init_user):
        location, reg_expr = TestRegexAbonent.get_test_args(TestRegexAbonent.path_select, "fio")
        RegexWrapper.regex(location, reg_expr, driver=driver_init_user)

    #@staticmethod
   # def test_regex_phone_number(driver_init_user):
    #    location, reg_expr = TestRegexAbonent.get_test_args(TestRegexAbonent.path_select, "phone_number")
     #   RegexWrapper.regex(location, reg_expr, driver=driver_init_user)

    @staticmethod
    def test_regex_address(driver_init_user):
        location, reg_expr = TestRegexAbonent.get_test_args(TestRegexAbonent.path_select, "address")
        RegexWrapper.regex(location, reg_expr, driver=driver_init_user)

    @staticmethod
    def test_regex_contractor_information(driver_init_user):
        location, reg_expr = TestRegexAbonent.get_test_args(TestRegexAbonent.path_select, "contractor_information")
        RegexWrapper.regex(location, reg_expr, driver=driver_init_user)

