import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from inenv.Lib.Utility import read_file_to_dictionary, wait_of_element_located_fix

path_fixture = 'D:\Fixtures\Fixture.yml'
path_searchselect = 'C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SearchSelectors.yml'

print('LOGGING: Enter conftest')


# Авторизация от администратора
@pytest.fixture
def driver_init_user():
    url = (read_file_to_dictionary(path_fixture)['TestConnection']['URL'])
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    print("LOGGING: Authentication")

    user_login = str(read_file_to_dictionary(path_fixture)['TestUsers'][3]['Login'])
    user_password = str(read_file_to_dictionary(path_fixture)['TestUsers'][3]['Password'])

    selector_login = str(read_file_to_dictionary(path_searchselect)['SelectorsAuthorization']['Locations'][0]['Location'])
    selector_password = str(read_file_to_dictionary(path_searchselect)['SelectorsAuthorization']['Locations'][1]['Location'])
    selector_button = str(read_file_to_dictionary(path_searchselect)['SelectorsAuthorization']['Locations'][2]['Location'])

    # Поиск и ожидание элементов и присваивание к переменным.
    time.sleep(3)
    input_username = wait_of_element_located_fix(selector=selector_login,  driver=driver)
    input_password = wait_of_element_located_fix(selector=selector_password, driver=driver)
    button_enter = wait_of_element_located_fix(selector=selector_button, driver=driver)
    # Действия с формами
    time.sleep(2)
    input_username.send_keys(user_login)
    time.sleep(2)
    input_password.send_keys(user_password)
    time.sleep(2)
    button_enter.send_keys(Keys.RETURN)
    time.sleep(4)

    selector_page_account = str(read_file_to_dictionary(path_searchselect)['Selectors_pages']['Locations'][1]['Location'])
    search_abonent = wait_of_element_located_fix(selector=selector_page_account, driver=driver)

    search_abonent.send_keys(Keys.RETURN)
    time.sleep(6)

    yield driver
    driver.close()

# @pytest.fixture
'''def full_init()
    driver_init()
    auth_user()'''
