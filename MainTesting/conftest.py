import pytest
import yaml
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from yaml.loader import SafeLoader
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Функция ожидания элементов
def wait_of_element_located(selector, driver_init):
    element = WebDriverWait(driver_init, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, selector)
        )
    )
    return element


# Вынесем инициализцию драйвера в отдельную фикстуру pytest
@pytest.fixture
def driver_init():
    with open('D:\Fixtures\Fixture.yml', encoding='utf-8') as fc:
        read_options = dict(yaml.load(fc, Loader=SafeLoader))
    url = (read_options['TestConnection']['URL'])
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    yield driver
    driver.close()


@pytest.fixture
def auth_user(driver_init):
    with open('D:\Fixtures\Fixture.yml', encoding='utf-8') as fd:
        # Load YAML data from the file
        read_options = dict(yaml.load(fd, Loader=SafeLoader))
    login_user = str(read_options['TestUsers'][1]['Login'])
    password_user = str(read_options['TestUsers'][1]['Password'])
    # Поиск и ожидание элементов и присваивание к переменным.
    input_username = wait_of_element_located(selector='#input_login_01', driver_init=driver_init)
    input_password = wait_of_element_located(selector='#input_password_01', driver_init=driver_init)
    button_enter = wait_of_element_located(selector='#btn_login_accept_01.btn.btn-primary.btn-modal',
                                           driver_init=driver_init)
    # Действия с формами
    time.sleep(2)
    input_username.send_keys(login_user)
    time.sleep(2)
    input_password.send_keys(password_user)
    time.sleep(2)
    button_enter.send_keys(Keys.RETURN)
    time.sleep(4)


@pytest.fixture
# переход на нужную старницу
def perechod(driver_init, auth_user):
    search_abonent = wait_of_element_located(selector='div#navbar_collapse_01 ul.nav.navbar-nav:nth-child(1) '
                                                      'li:nth-child(2)>a', driver_init=driver_init)
    search_abonent.send_keys(Keys.RETURN)
    time.sleep(6)
