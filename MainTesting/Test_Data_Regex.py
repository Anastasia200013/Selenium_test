import time
from pathlib import Path
from selenium.webdriver.common.keys import Keys
from OnBeforeTest.conftest import driver_init_user
from inenv.Lib.Utility import read_file_to_dictionary, wait_of_element_located_fix, regex

home = Path.cwd()
path_searchselect = 'C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SearchSelectors.yml'
path_testcases = 'C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\TestCases\\Test.yml'


# Тест
def test_regex_abonent(driver_init_user):
    file_name = str(read_file_to_dictionary(path_searchselect)['Selectors']['FileTest'])
    selector_ab = str(read_file_to_dictionary(path_searchselect)['Selectors']['Locations'][0]['Location'])
    # selector_ow = str(read_data_slcrt['Selectors']['StrOwnerid'])

    test_reg_ab = str(read_file_to_dictionary(file_name)['TestDescription']['Tests'][0]['Exp'])
    # test_reg_ow = str(read_data_test['TestDescription']['TestInfoOwner'])

    regex(selector_ab, test_reg_ab, driver=driver_init_user)


def test_regex_fio(driver_init_user):
    file_name = str(read_file_to_dictionary(path_searchselect)['Selectors']['FileTest'])
    selector_fio = str(read_file_to_dictionary(path_searchselect)['Selectors']['Locations'][1]['Location'])

    test_reg_fio = str(read_file_to_dictionary(file_name)['TestDescription']['Tests'][1]['Exp'])

    regex(selector_fio, test_reg_fio, driver=driver_init_user)


def test_regex_address(driver_init_user):
    file_name = str(read_file_to_dictionary(path_searchselect)['Selectors']['FileTest'])
    selector_address = str(read_file_to_dictionary(path_searchselect)['Selectors']['Locations'][2]['Location'])

    test_reg_address = str(read_file_to_dictionary(file_name)['TestDescription']['Tests'][2]['Exp'])

    regex(selector_address, test_reg_address, driver=driver_init_user)


def test_go_page(driver_init_user):
    selector_page_account = str(read_file_to_dictionary(path_searchselect)['Selectors_pages']['Locations'][2]['Location'])
    search_abonent = wait_of_element_located_fix(selector=selector_page_account, driver=driver_init_user)
    search_abonent.send_keys(Keys.RETURN)
    time.sleep(6)

    selector_page_account = str(read_file_to_dictionary(path_searchselect)['Selectors_pages']['Locations'][3]['Location'])
    search_abonent = wait_of_element_located_fix(selector=selector_page_account, driver=driver_init_user)
    search_abonent.send_keys(Keys.RETURN)
    time.sleep(6)


'''def view_main_page():
    ## common page info test

def test_view_main_page_cashier(cashier_login_fixture):
    view_main_page()
    ##cashier-special testing of main page'''


if __name__ == '__main__':
    test_regex_abonent(driver_init_user=driver_init_user)
    '''test_regex_fio(driver_init_admin=driver_init_admin)
    test_regex_address(driver_init_admin=driver_init_admin)
    test_go_page(driver_init_admin=driver_init_admin)'''


