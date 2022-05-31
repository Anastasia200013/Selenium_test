from inenv.Lib.SQLWrapper import SQLWrapper
from OnBeforeTest.conftest import driver_init_mainpage
from inenv.Lib.Utility import Utility
import pathlib
from pathlib import Path

class TestSQLOrganization(SQLWrapper):
    class_test_name = "Organization"
   # path_searchselect = '\\selenium-test\\SearchSelect\\SelectorsOrganization.yml'
    path_select = Path(pathlib.Path.home(), 'PycharmProjects', 'selenium-test', 'SearchSelect', 'SelectorsOrganization.yml')

    @staticmethod
    def test_request_amount_accountcd(driver_init_mainpage, record_xml_attribute):
        location, request_sql = TestSQLOrganization.get_test_components(TestSQLOrganization.path_select, "amount_accountcd")
        print(location, request_sql)
        SQLWrapper.check_request(location, request_sql, driver=driver_init_mainpage)

    @staticmethod
    def test_request_amount_houses(driver_init_mainpage, record_xml_attribute):
        location, request_sql = TestSQLOrganization.get_test_components(TestSQLOrganization.path_select, "amount_houses")
        SQLWrapper.check_request(location, request_sql, driver=driver_init_mainpage)

    @staticmethod
    def test_request_amount_services(driver_init_mainpage, record_xml_attribute):
        location, request_sql = TestSQLOrganization.get_test_components(TestSQLOrganization.path_select, "amount_services")
        SQLWrapper.check_request(location, request_sql, driver=driver_init_mainpage)

  #  @staticmethod
   # def test_request_accrued_on_month(driver_init_user):
   #     location, request_sql = TestRegexOrganization.get_test_components(TestRegexOrganization.path_searchselect, "accrued_on_month")
   #     SQLWrapper.check_request(location, request_sql, driver=driver_init_user)

   # @staticmethod
   # def test_request_accrued_on_closet_until_month(driver_init_user):
    #    location, request_sql = TestRegexOrganization.get_test_components(TestRegexOrganization.path_searchselect, "accrued_on_closet_until_month")
    #    SQLWrapper.check_request(location, request_sql, driver=driver_init_user)
