from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def test_passing():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('http://192.168.50.10:8510/?page=AboutProject')
    time.sleep(2)
    search_home = driver.find_element(By.CSS_SELECTOR, "li.ng-binding.ng-scope a").click()
    time.sleep(5)

    login_1 = driver.find_element(By.CSS_SELECTOR, '#input_login_01').send_keys('Sysdba')

    parol_1 = driver.find_element(By.CSS_SELECTOR, '#input_password_01').send_keys('305')

    time.sleep(3)
    button_enter = driver.find_element(By.CSS_SELECTOR, '#btn_login_accept_01.btn.btn-primary.btn-modal').click()

    time.sleep(5)
    search_directory = driver.find_element(By.CSS_SELECTOR, 'ul.nav.navbar-nav li.ng-scope:nth-child(7) a').click()

    time.sleep(3)
    search_col_record = driver.find_element(By.CSS_SELECTOR, 'div#pg-balances-top div.btn.btn-default.'
                                                             'pull-right.disabled  b.ng-binding')

    assert search_col_record.text == '2982'

    def test_check_results_count(driver):
        driver.execute_script("window.scrollBy(0, 350);")
        time.sleep(3)
        search_list = driver.find_elements(By.CSS_SELECTOR, 'table.table.table-bordered.table-hover tbody tr')
        return len(search_list) <= 20

    test_check_results_count(driver)

    button_option = driver.find_element(By.CSS_SELECTOR, 'div.container.ng-scope div.ng-isolate-scope '
                                                         'div.div-scroll-x.col-sm-10 div.ng-isolate-scope '
                                                         'div.btn-group.bootstrap-select.pull-right.'
                                                         'inline-control.ng-pristine.ng-untouched.ng-valid '
                                                         'button.btn.dropdown-toggle.selectpicker.btn-default').click()
    time.sleep(3)
    button_option = driver.find_element(By.CSS_SELECTOR, 'div.container.ng-scope div#pg-balances-top '
                                                         'div.btn-group.bootstrap-select.pull-right.inline-control.'
                                                         'ng-pristine.ng-untouched.ng-valid div.dropdown-menu.open '
                                                         'ul.dropdown-menu.inner.selectpicker li:nth-child(3) a').click()
    time.sleep(5)

    def test_check_results_count(driver):
        driver.execute_script("window.scrollBy(0, 350);")
        time.sleep(3)
        inner_search_rez = driver.find_elements(By.CSS_SELECTOR, 'div.container.ng-scope div.ng-isolate-scope '
                                                                 'div.div-scroll-x.col-sm-10 div.ng-isolate-scope '
                                                                 'table.table.table-bordered.table-hover tbody tr')
        return len(inner_search_rez) <= 50

    test_check_results_count(driver)

    driver.execute_script("window.scrollBy(0, -450);")
    time.sleep(3)
    dropdown_list = driver.find_element(By.CSS_SELECTOR, 'div.row div.col-sm-3.hidden-xs '
                                                         'div.panel-heading.pointer-cursor:nth-child(1)').click()
    time.sleep(3)
    list_substr = driver.find_element(By.CSS_SELECTOR, 'div.panel-body.collapse.in input')
    list_substr.send_keys('Содержание жилья')
    time.sleep(1)
    button_ok = driver.find_element(By.CSS_SELECTOR, 'div.form-group-buttons button.btn.btn-primary').click()
    time.sleep(5)
    search_price = driver.find_element(By.CSS_SELECTOR, 'li.pointer-cursor.ng-scope:nth-child(2)').click()
