from inenv.Lib.SQLWrapper import SQLWrapper
from OnBeforeTest.conftest import driver_init_user
from inenv.Lib.Utility import Utility
from OnBeforeTest.conftest import driver_init_Counter_regim
import pathlib
from pathlib import Path

class TestSQLCounter(SQLWrapper):
    class_test_name = "Counter"
    #path_searchselect = '\\selenium-test\\SearchSelect\\SelectorsCounter.yml'
    path_select = Path(pathlib.Path.home(), 'PycharmProjects', 'selenium-test', 'SearchSelect', 'SelectorsCounter.yml')

    @staticmethod
    def test_request_registration_date(driver_init_Counter):
        location, request_sql = TestSQLCounter.get_test_components(TestSQLCounter.path_select, "registration_date")
        SQLWrapper.check_request(location, request_sql, driver=driver_init_Counter)

    # @staticmethod
    # def test_request_indications_now(driver_init_Counter):
    #     location, request_sql = TestRegexOrganization.get_test_components(TestRegexOrganization.path_searchselect, "indications_now")
    #     SQLWrapper.check_request(location, request_sql, driver=driver_init_Counter)
    #
    # @staticmethod
    # def test_request_initial_indications(driver_init_Counter):
    #     location, request_sql = TestRegexOrganization.get_test_components(TestRegexOrganization.path_searchselect, "initial_indications")
    #     SQLWrapper.check_request(location, request_sql, driver=driver_init_Counter)
    #
    # @staticmethod
    # def test_request_next_verification_date(driver_init_Counter):
    #     location, request_sql = TestRegexOrganization.get_test_components(TestRegexOrganization.path_searchselect, "next_verification_date")
    #     SQLWrapper.check_request(location, request_sql, driver=driver_init_Counter)
    #
    # @staticmethod
    # def test_request_last_verification_date(driver_init_Counter):
    #     location, request_sql = TestRegexOrganization.get_test_components(TestRegexOrganization.path_searchselect, "last_verification_date")
    #     SQLWrapper.check_request(location, request_sql, driver=driver_init_Counter)
    #
    # @staticmethod
    # def test_request_date_seal(driver_init_Counter):
    #     location, request_sql = TestRegexOrganization.get_test_components(TestRegexOrganization.path_searchselect, "date_seal")
    #     SQLWrapper.check_request(location, request_sql, driver=driver_init_Counter)

    @staticmethod
    def test_regex_regime(driver_init_Counter_regim):
        location, request_sql = TestSQLCounter.get_test_components(TestSQLCounter.path_select, "regime")
        SQLWrapper.check_list(location, request_sql, driver=driver_init_Counter_regim)
