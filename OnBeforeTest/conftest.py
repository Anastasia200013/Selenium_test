from selenium.webdriver.support import expected_conditions as EC
import pathlib
from pathlib import Path
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from inenv.Lib.Utility import Utility#Utility.read_file_to_dictionary, wait_of_element_located_fix

#path_fixture = '\\selenium-test\\Fixture.yml'
path_fixture1 = Path(pathlib.Path.cwd(), 'Fixture.yml')
#path_searchselect = '\\selenium-test\\SearchSelect\\SearchSelectors.yml'
path_searchselect1 = Path(pathlib.Path.home(), 'PycharmProjects', 'selenium-test', 'SearchSelect', 'SearchSelectors.yml')

print('LOGGING: Enter conftest')


@pytest.fixture
def driver_init_phone():
    print(path_searchselect1)
    print(path_searchselect1)
    url = (Utility.read_file_to_dictionary(path_fixture1)['TestConnection']['URL'])
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    print("LOGGING: Authentication")

    user_login = str(Utility.read_file_to_dictionary(path_fixture1)['TestUsers'][3]['Login'])
    user_password = str(Utility.read_file_to_dictionary(path_fixture1)['TestUsers'][3]['Password'])

    selector_login = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][0]['Location'])
    selector_password = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][1]['Location'])
    selector_button = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][2]['Location'])

    # Поиск и ожидание элементов и присваивание к переменным.
    time.sleep(3)
    input_username = Utility.wait_of_element_located_fix(selector=selector_login,  driver=driver)
    input_password = Utility.wait_of_element_located_fix(selector=selector_password, driver=driver)
    button_enter = Utility.wait_of_element_located_fix(selector=selector_button, driver=driver)
    # Действия с формами
    time.sleep(2)
    input_username.send_keys(user_login)
    time.sleep(2)
    input_password.send_keys(user_password)
    time.sleep(2)
    button_enter.send_keys(Keys.RETURN)
    time.sleep(4)

    selector_page_accounts = str(Utility.read_file_to_dictionary(path_searchselect1)['Selectors_pages']['Locations'][1]['Location'])
    search_abonents = Utility.wait_of_element_located_fix(selector=selector_page_accounts, driver=driver)

    search_abonents.click()
    time.sleep(6)

    selector_page_account = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][3]['Location'])
    search_abonent = Utility.wait_of_element_located_fix(selector=selector_page_account, driver=driver)

    search_abonent.send_keys(Keys.RETURN)
    time.sleep(6)

    yield driver
    driver.close()


# Авторизация от администратора переход на страницу абонентов
@pytest.fixture
def driver_init_user():
    url = (Utility.read_file_to_dictionary(path_fixture1)['TestConnection']['URL'])
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    print("LOGGING: Authentication")

    user_login = str(Utility.read_file_to_dictionary(path_fixture1)['TestUsers'][0]['Login'])
    user_password = str(Utility.read_file_to_dictionary(path_fixture1)['TestUsers'][0]['Password'])

    selector_login = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][0]['Location'])
    selector_password = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][1]['Location'])
    selector_button = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][2]['Location'])

    # Поиск и ожидание элементов и присваивание к переменным.
    time.sleep(3)
    input_username = Utility.wait_of_element_located_fix(selector=selector_login,  driver=driver)
    input_password = Utility.wait_of_element_located_fix(selector=selector_password, driver=driver)
    button_enter = Utility.wait_of_element_located_fix(selector=selector_button, driver=driver)
    # Действия с формами
    time.sleep(2)
    input_username.send_keys(user_login)
    time.sleep(2)
    input_password.send_keys(user_password)
    time.sleep(2)
    button_enter.send_keys(Keys.RETURN)
    time.sleep(4)

    selector_page_account = str(Utility.read_file_to_dictionary(path_searchselect1)['Selectors_pages']['Locations'][1]['Location'])
    search_abonent = Utility.wait_of_element_located_fix(selector=selector_page_account, driver=driver)

    search_abonent.click()
    time.sleep(6)

    yield driver
    driver.close()


# Авторизация от администратора главная страница
@pytest.fixture
def driver_init_mainpage():
    url = (Utility.read_file_to_dictionary(path_fixture1)['TestConnection']['URL'])
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    print("LOGGING: Authentication")

    user_login = str(Utility.read_file_to_dictionary(path_fixture1)['TestUsers'][0]['Login'])
    user_password = str(Utility.read_file_to_dictionary(path_fixture1)['TestUsers'][0]['Password'])

    selector_login = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][0]['Location'])
    selector_password = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][1]['Location'])
    selector_button = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][2]['Location'])

    # Поиск и ожидание элементов и присваивание к переменным.
    time.sleep(3)
    input_username = Utility.wait_of_element_located_fix(selector=selector_login,  driver=driver)
    input_password = Utility.wait_of_element_located_fix(selector=selector_password, driver=driver)
    button_enter = Utility.wait_of_element_located_fix(selector=selector_button, driver=driver)
    # Действия с формами
    time.sleep(2)
    input_username.send_keys(user_login)
    time.sleep(2)
    input_password.send_keys(user_password)
    time.sleep(2)
    button_enter.send_keys(Keys.RETURN)
    time.sleep(4)

    yield driver
    driver.close()


# Авторизация от администратора главная страница
@pytest.fixture
def driver_init_Counter():
    url = (Utility.read_file_to_dictionary(path_fixture1)['TestConnection']['URL'])
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    print("LOGGING: Authentication")

    user_login = str(Utility.read_file_to_dictionary(path_fixture1)['TestUsers'][0]['Login'])
    user_password = str(Utility.read_file_to_dictionary(path_fixture1)['TestUsers'][0]['Password'])

    selector_login = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][0]['Location'])
    selector_password = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][1]['Location'])
    selector_button = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][2]['Location'])

    # Поиск и ожидание элементов и присваивание к переменным.
    time.sleep(3)
    input_username = Utility.wait_of_element_located_fix(selector=selector_login,  driver=driver)
    input_password = Utility.wait_of_element_located_fix(selector=selector_password, driver=driver)
    button_enter = Utility.wait_of_element_located_fix(selector=selector_button, driver=driver)
    # Действия с формами
    time.sleep(5)
    input_username.send_keys(user_login)
    time.sleep(5)
    input_password.send_keys(user_password)
    time.sleep(5)
    button_enter.send_keys(Keys.RETURN)
    time.sleep(15)

    selector_page_accounts = str(Utility.read_file_to_dictionary(path_searchselect1)['Selectors_pages']['Locations'][1]['Location'])
    search_abonents = Utility.wait_of_element_located_fix(selector=selector_page_accounts, driver=driver)

    search_abonents.click()
    time.sleep(10)

    selector_page_account = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][3]['Location'])
    search_abonent = Utility.wait_of_element_located_fix(selector=selector_page_account, driver=driver)

    search_abonent.send_keys(Keys.RETURN)
    time.sleep(25)

    selector_page_count = str(Utility.read_file_to_dictionary(path_searchselect1)['Selectors_pages']['Locations'][2]['Location'])
    search_count = Utility.wait_of_element_located_fix(selector=selector_page_count, driver=driver)

    search_count.click()
    time.sleep(6)

    yield driver
    driver.close()

# Авторизация от администратора главная страница
@pytest.fixture
def driver_init_Counter_regim():
    url = (Utility.read_file_to_dictionary(path_fixture1)['TestConnection']['URL'])
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    print("LOGGING: Authentication")

    user_login = str(Utility.read_file_to_dictionary(path_fixture1)['TestUsers'][0]['Login'])
    user_password = str(Utility.read_file_to_dictionary(path_fixture1)['TestUsers'][0]['Password'])

    selector_login = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][0]['Location'])
    selector_password = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][1]['Location'])
    selector_button = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][2]['Location'])

    # Поиск и ожидание элементов и присваивание к переменным.
    time.sleep(3)
    input_username = Utility.wait_of_element_located_fix(selector=selector_login,  driver=driver)
    input_password = Utility.wait_of_element_located_fix(selector=selector_password, driver=driver)
    button_enter = Utility.wait_of_element_located_fix(selector=selector_button, driver=driver)
    # Действия с формами
    time.sleep(2)
    input_username.send_keys(user_login)
    time.sleep(2)
    input_password.send_keys(user_password)
    time.sleep(2)
    button_enter.send_keys(Keys.RETURN)
    time.sleep(4)

    selector_page_accounts = str(Utility.read_file_to_dictionary(path_searchselect1)['Selectors_pages']['Locations'][1]['Location'])
    search_abonents = Utility.wait_of_element_located_fix(selector=selector_page_accounts, driver=driver)

    search_abonents.click()
    time.sleep(6)

    selector_page_account = str(Utility.read_file_to_dictionary(path_searchselect1)['SelectorsAuthorization']['Locations'][3]['Location'])
    search_abonent = Utility.wait_of_element_located_fix(selector=selector_page_account, driver=driver)

    search_abonent.send_keys(Keys.RETURN)
    time.sleep(6)

    selector_page_count = str(Utility.read_file_to_dictionary(path_searchselect1)['Selectors_pages']['Locations'][2]['Location'])
    search_count = Utility.wait_of_element_located_fix(selector=selector_page_count, driver=driver)

    search_count.click()
    time.sleep(6)

    selector_page_count_regim = str(Utility.read_file_to_dictionary(path_searchselect1)['Selectors_pages']['Locations'][3]['Location'])
    search_count_regim = Utility.wait_of_element_located_fix(selector=selector_page_count_regim, driver=driver)

    search_count_regim.click()
    time.sleep(6)

    yield driver
    driver.close()
# @pytest.fixture
'''def full_init()
    driver_init()
    auth_user()'''
