import yaml
import time
import pytest
from yaml.loader import SafeLoader
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture
def options_get():
    with open('D:\Fixtures\Fixture.yml', encoding='utf-8') as f:
        # Load YAML data from the file
        read_options = dict(yaml.load(f, Loader=SafeLoader))

        url = (read_options['TestConnection']['URL'])
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        return driver


def test_authoriz(options_get):
    with open('D:\Fixtures\Fixture.yml', encoding='utf-8') as f:
        # Load YAML data from the file
        read_options = dict(yaml.load(f, Loader=SafeLoader))

        login_user = str(read_options['TestUsers']['Login'])
        password_user = str(read_options['TestUsers']['Password'])

        time.sleep(2)
        search_home = options_get.find_element(By.CSS_SELECTOR, "li.ng-binding.ng-scope a").click()
        time.sleep(3)
        login_1 = options_get.find_element(By.CSS_SELECTOR, '#input_login_01').send_keys(login_user)
        parol_1 = options_get.find_element(By.CSS_SELECTOR, '#input_password_01').send_keys(password_user)
        time.sleep(3)
        button_enter = options_get.find_element(By.CSS_SELECTOR, '#btn_login_accept_01.btn.btn-primary.'
                                                                 'btn-modal').click()

        time.sleep(3)
        search_abonent = options_get.find_element(By.CSS_SELECTOR, 'div#navbar_collapse_01'
                                                                   ' ul.nav.navbar-nav:nth-child(1)'
                                                                   ' li:nth-child(2)>a').click()
        time.sleep(3)
