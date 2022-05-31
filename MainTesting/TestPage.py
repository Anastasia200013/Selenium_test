from inenv.Lib.Selector import Selectors
from inenv.Lib.Selector import Location
from inenv.Lib.Utility import Utility
from inenv.Lib.RegexWrapper import RegexWrapper
from OnBeforeTest.conftest import driver_init_mainpage, driver_init_user

class TestPage():
    class_test_name = "Abonent"
    path_searchselect = '\\selenium-test\\SearchSelect\\SelectorsPage.yml'

    @staticmethod
    def get_test_args(path_searchselect, field_test_name):
        selector = Selectors.load(path_searchselect)
        location = Location.find_by_field_name(selector.locations, field_test_name).location
        return location

    @staticmethod
    def test_regex_Main(driver_init_user):
        location = TestPage.get_test_args(TestPage.path_searchselect, "Main")
        elenent = RegexWrapper.page(selector=location, driver=driver_init_user)

    @staticmethod
    def test_regex_ButtonPortal(driver_init_mainpage):
        location = TestPage.get_test_args(TestPage.path_searchselect, "ButtonPortal")
        elenent = RegexWrapper.page(selector=location, driver=driver_init_mainpage)

    @staticmethod
    def test_regex_WindowOrganization(driver_init_mainpage):
        location = TestPage.get_test_args(TestPage.path_searchselect, "WindowOrganization")
        elenent = RegexWrapper.page(selector=location, driver=driver_init_mainpage)

    @staticmethod
    def test_regex_WindowServiceZone(driver_init_mainpage):
        location = TestPage.get_test_args(TestPage.path_searchselect, "WindowServiceZone")
        elenent = RegexWrapper.page(selector=location, driver=driver_init_mainpage)

    @staticmethod
    def test_regex_WindowNews(driver_init_mainpage):
        location = TestPage.get_test_args(TestPage.path_searchselect, "WindowNews")
        elenent = RegexWrapper.page(selector=location, driver=driver_init_mainpage)

    @staticmethod
    def test_regex_WindowNews(driver_init_mainpage):
        location = TestPage.get_test_args(TestPage.path_searchselect, "WindowNews")
        elenent = RegexWrapper.page(selector=location, driver=driver_init_mainpage)

    @staticmethod
    def test_regex_WindowAccrualsAndPayment(driver_init_mainpage):
        location = TestPage.get_test_args(TestPage.path_searchselect, "WindowAccrualsAndPayment")
        elenent = RegexWrapper.page(selector=location, driver=driver_init_mainpage)

    @staticmethod
    def test_regex_DropdownToggleChanges(driver_init_user):
        location = TestPage.get_test_args(TestPage.path_searchselect, "DropdownToggleChanges")
        elenent = RegexWrapper.page(selector=location, driver=driver_init_user)

    @staticmethod
    def test_regex_DropdownToggleOperetion(driver_init_user):
        location = TestPage.get_test_args(TestPage.path_searchselect, "DropdownToggleOperetion")
        elenent = RegexWrapper.page(selector=location, driver=driver_init_user)

    @staticmethod
    def test_regex_DropdownToggleForm(driver_init_user):
        location = TestPage.get_test_args(TestPage.path_searchselect, "DropdownToggleForm")
        elenent = RegexWrapper.page(selector=location, driver=driver_init_user)

    @staticmethod
    def test_regex_DropdownToggleReports(driver_init_user):
        location = TestPage.get_test_args(TestPage.path_searchselect, "DropdownToggleReports")
        elenent = RegexWrapper.page(selector=location, driver=driver_init_user)

    @staticmethod
    def test_regex_DropdownToggleDocumentation(driver_init_user):
        location = TestPage.get_test_args(TestPage.path_searchselect, "DropdownToggleDocumentation")
        elenent = RegexWrapper.page(selector=location, driver=driver_init_user)

    @staticmethod
    def test_regex_TableAbonents(driver_init_user):
        location = TestPage.get_test_args(TestPage.path_searchselect, "TableAbonents")
        elenent = RegexWrapper.page(selector=location, driver=driver_init_user)


