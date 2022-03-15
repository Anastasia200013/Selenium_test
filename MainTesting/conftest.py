import yaml
import pytest
from yaml.loader import SafeLoader
from selenium import webdriver


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

