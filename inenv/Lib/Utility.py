import pytest
import yaml
import fdb
import sqlite3
from datetime import timedelta, datetime
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from yaml.loader import SafeLoader


# Функция ожидания элементов
from DomainClass.Abonent import Abonent
from inenv.Lib.Selector import Selectors, Location
from inenv.Lib.Case import TestDescription, Test


class Utility:

    @staticmethod
    def wait_of_element_located_fix(selector, driver):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, selector)
            )
        )
        return element

    @staticmethod
    def read_file_to_dictionary(file_name):
         with open(file_name, 'r', encoding='utf-8') as h:
             # Загрузка YAML данных из файла
             read_data_slcrt = dict(yaml.load(h, Loader=SafeLoader))
             return read_data_slcrt

    @staticmethod
    def write_dictionary_to_file(file_name, dictionary):
         with open(file_name, 'w') as f:
             yaml.dump(dictionary, f)

    @staticmethod
    def go_to_pages(selector, driver_init_admin):
        search_abonent = Utility.wait_of_element_located_fix(selector=selector, driver=driver_init_admin)
        search_abonent.send_keys(Keys.RETURN)
        time.sleep(6)

    @staticmethod
    def generate_dict_selectors(d):
        key = str(list(d.keys())[0])
        new_d = {"Selectors": {
             "FileTest": "",
             "Type": key,
             "Locations": [{
                 "FieldName": str(k),
                 "Location": ""}
                 for k in d[key].keys()]
             }
         }
        return new_d

    @staticmethod
    def connect_bd(path):
        # Соединение
        con = fdb.connect(database=path, user='SYSDBA', password='masterkey')   #'C:\\Users\\a.petrova\\Desktop\\BDSEL\\ABONENT_3.fdb'
        return con

