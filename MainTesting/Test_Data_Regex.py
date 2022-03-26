from pathlib import Path
from OnBeforeTest.conftest import driver_init
from Utility import regex, read_file_to_dictionary


home = Path.cwd()
path_searchselect = 'C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SearchSelectors.yml'
path_testcases = Path('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\TestCases\\Test.yml')


# Тест
def test_regular_exp(driver_init):
    # file_name = str(read_file_to_dictionary(path_testcases)['TestDescription']['FileSelectors'])
    test_reg_ab = str(read_file_to_dictionary(path_testcases)['TestDescription']['Tests'][0]['Exp'])
    test_reg_fio = str(read_file_to_dictionary(path_testcases)['TestDescription']['Tests'][1]['Exp'])
    test_reg_address = str(read_file_to_dictionary(path_testcases)['TestDescription']['Tests'][2]['Exp'])
    # test_reg_ow = str(read_data_test['TestDescription']['TestInfoOwner'])
    print(test_reg_ab, ';', test_reg_fio, ';', test_reg_address)

    selector_ab = str(read_file_to_dictionary(path_searchselect)['Selectors']['Locations'][0]['Location'])
    selector_fio = str(read_file_to_dictionary(path_searchselect)['Selectors']['Locations'][1]['Location'])
    selector_address = str(read_file_to_dictionary(path_searchselect)['Selectors']['Locations'][2]['Location'])
    # selector_ow = str(read_data_slcrt['Selectors']['StrOwnerid'])
    print(selector_ab, ';', selector_fio, ';', selector_address)

    regex(selector_ab, test_reg_ab, driver_init=driver_init)
    regex(selector_fio, test_reg_fio, driver_init=driver_init)
    regex(selector_address, test_reg_address, driver_init=driver_init)

    print(home)


'''def view_main_page():
    ## common page info test

def test_view_main_page_cashier(cashier_login_fixture):
    view_main_page()
    ##cashier-special testing of main page'''


if __name__ == '__main__':
    test_regular_exp(driver_init=driver_init)
