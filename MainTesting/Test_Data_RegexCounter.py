from inenv.Lib.RegexWrapper import RegexWrapper
from OnBeforeTest.conftest import driver_init_Counter
import pathlib
from pathlib import Path

class TestRegexCounter(RegexWrapper):
    class_test_name = "Counter"
    path_select = Path(pathlib.Path.home(), 'PycharmProjects', 'selenium-test', 'SearchSelect', 'SelectorsCounter.yml')

    #@staticmethod
    #def test_regex_serviceid(driver_init_user):
     #   location, reg_expr = TestRegexOrganization.get_test_args(TestRegexOrganization.path_searchselect, "serviceid")
      #  RegexWrapper.regex(location, reg_expr, driver=driver_init_user)

    @staticmethod
    def test_regex_mark(driver_init_Counter):
        location, reg_expr = TestRegexCounter.get_test_args(TestRegexCounter.path_select, "mark")
        RegexWrapper.regex(location, reg_expr, driver=driver_init_Counter)

    @staticmethod
    def test_regex_counter_name(driver_init_Counter):
        location, reg_expr = TestRegexCounter.get_test_args(TestRegexCounter.path_select, "counter_name")
        RegexWrapper.regex(location, reg_expr, driver=driver_init_Counter)

    @staticmethod
    def test_regex_serial_number(driver_init_Counter):
        location, reg_expr = TestRegexCounter.get_test_args(TestRegexCounter.path_select, "serial_number")
        RegexWrapper.regex(location, reg_expr, driver=driver_init_Counter)

    @staticmethod
    def test_regex_installation_location(driver_init_Counter):
        location, reg_expr = TestRegexCounter.get_test_args(TestRegexCounter.path_select, "installation_location")
        RegexWrapper.regex(location, reg_expr, driver=driver_init_Counter)

    @staticmethod
    def test_regex_status(driver_init_Counter):
        location, reg_expr = TestRegexCounter.get_test_args(TestRegexCounter.path_select, "status")
        RegexWrapper.regex(location, reg_expr, driver=driver_init_Counter)

    # @staticmethod
    # def test_regex_number_seal(driver_init_Counter):
    #     location, reg_expr = TestRegexCounter.get_test_args(TestRegexCounter.path_select, "number_seal")
    #     RegexWrapper.regex(location, reg_expr, driver=driver_init_Counter)
    #
    # @staticmethod
    # def test_regex_type_seal(driver_init_Counter):
    #     location, reg_expr = TestRegexCounter.get_test_args(TestRegexCounter.path_select, "type_seal")
    #     RegexWrapper.regex(location, reg_expr, driver=driver_init_Counter)

