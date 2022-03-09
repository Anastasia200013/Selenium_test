import yaml
import re
import time
from yaml.loader import SafeLoader
from selenium.webdriver.common.by import By
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('http://192.168.50.10:8510')


# Authorization and transition to the page of subscribers
def test_authoriz(driv):
    time.sleep(2)
    search_home = driv.find_element(By.CSS_SELECTOR, "li.ng-binding.ng-scope a").click()
    time.sleep(3)
    login_1 = driv.find_element(By.CSS_SELECTOR, '#input_login_01').send_keys('User_028')
    parol_1 = driv.find_element(By.CSS_SELECTOR, '#input_password_01').send_keys('0')
    time.sleep(3)
    button_enter = driv.find_element(By.CSS_SELECTOR, '#btn_login_accept_01.btn.btn-primary.btn-modal').click()
    time.sleep(3)
    search_abonent = driv.find_element(By.CSS_SELECTOR, 'div#navbar_collapse_01 ul.nav.navbar-nav:nth-child(1)'
                                                        ' li:nth-child(2)>a').click()
    time.sleep(3)


def test_regex(driver, field_abonentcd, regex_str):
    time.sleep(3)
    search_element = driver.find_element(By.CSS_SELECTOR, field_abonentcd)
    element = search_element.text
    check_test = re.fullmatch(regex_str, element)
    print('YES' if check_test else 'NO')

try:
    with open('Test.yml', encoding='utf-8') as f:
      # Load YAML data from the file
      read_data_test = dict(yaml.load(f, Loader=SafeLoader))

    fileName = str(read_data_test['TestDescription']['FileSelectors'])
    testRegAc = str(read_data_test['TestDescription']['TestAccount'])
    testRegFIO = str(read_data_test['TestDescription']['TestFIO'])
    testRegAddress = str(read_data_test['TestDescription']['TestAddress'])
    testRegOw = str(read_data_test['TestDescription']['TestInfoOwner'])
    print(testRegAc, ';', testRegFIO, ';', testRegAddress, ';', testRegOw)

    with open(fileName, encoding='utf-8') as h:
      # Load YAML data from the file
      read_data_slcrt = dict(yaml.load(h, Loader=SafeLoader))

    selectorAb = str(read_data_slcrt['Selectors']['StrAccountcd'])
    selectorFIO = str(read_data_slcrt['Selectors']['StrFIO'])
    selectorAddress = str(read_data_slcrt['Selectors']['StrAddressString'])
    selectorOw = str(read_data_slcrt['Selectors']['StrOwnerid'])

    test_authoriz(driver)
    test_regex(driver, selectorAb, testRegAc)
    test_regex(driver, selectorFIO, testRegFIO)
    test_regex(driver, selectorAddress, testRegAddress)
    test_regex(driver, selectorOw, testRegOw)

except FileNotFoundError:
    print('Файл или директория не существует.')

finally:
    # закрываем браузер после всех манипуляций
    driver.quit()
