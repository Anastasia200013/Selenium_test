from inenv.Lib.RegexWrapper import RegexWrapper
from OnBeforeTest.conftest import driver_init_mainpage
from inenv.Lib.Utility import Utility
import pathlib
from pathlib import Path

class TestRegexOrganization(RegexWrapper):
    class_test_name = "Organization"
    #path_searchselect = '\\selenium-test\\SearchSelect\\SelectorsOrganization.yml'
    path_select = Path(pathlib.Path.home(), 'PycharmProjects', 'selenium-test', 'SearchSelect', 'SelectorsOrganization.yml')
    @staticmethod
    def test_regex_contractor_id(driver_init_mainpage):
        location, reg_expr = TestRegexOrganization.get_test_args(TestRegexOrganization.path_select, "contractor_id")
        RegexWrapper.regex(location, reg_expr, driver=driver_init_mainpage)

    @staticmethod
    def test_regex_contractor_name(driver_init_mainpage):
        location, reg_expr = TestRegexOrganization.get_test_args(TestRegexOrganization.path_select, "contractor_name")
        RegexWrapper.regex(location, reg_expr, driver=driver_init_mainpage)


