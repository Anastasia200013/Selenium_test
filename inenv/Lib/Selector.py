from typing import List
import yaml
from inenv.Lib.Serialization import Serialization
from DomainClass.Organization import Organization
from DomainClass.Counter import Counter
from DomainClass.Page import Page


class Location:
    field_name: str
    location: str
    #name_element: str
    #name_page: str

    def __init__(self, field_name: str, location: str) -> None:
        self.field_name = field_name
        self.location = location
        #self.name_element = name_element
        #self.name_page = name_page


    def __repr__(self):
        return f"field_name:{self.field_name}, location:{self.location}"

    @staticmethod
    def find_by_field_name(locations, field_name):
        for location in locations:
            if location.field_name == field_name:
                return location


class Selectors(Serialization):
    file_test: str
    type: str
    locations: List[Location]
    path_searchselect = '\\selenium-test\\SearchSelect\\SearchSelectors.yml'

    def __init__(self, file_test: str, type: str, locations: List[Location]) -> None:
        self.file_test = file_test
        self.type = type
        self.locations = locations

    @staticmethod
    def generate(some_class):
        obj = Selectors('', some_class.__name__, [Location(field_name, "")
                                            for field_name in list(some_class.__dict__["__annotations__"].keys())])
        return obj

    # @staticmethod
    # def generate_values(some_class):
    #     with open('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\Domain\\pages.yml', 'r', encoding='utf-8') as h:
    #         # Загрузка YAML данных из файла
    #         read_data_slcrt = dict(yaml.load(h, Loader=yaml.Loader))
    #     obj = Selectors('', some_class.__name__,[Location.name_page,"" [Location(name_element, "")
    #                                               for name_element in
    #                                               list(read_data_slcrt.values())]])
    #     return obj


#selectors = Selectors.generate(Organization)
#selectors.save(selectors, 'C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SelectorsOrganization.yml')
#selectors2 = Selectors.load('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SelectorsOrganization.yml')
#print('hgkguk', selectors2.__dir__)
#print('dredhk', selectors.__dict__)
#selectors = Selectors.generate(Counter)
#selectors.save(selectors, 'C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SelectorsCounter.yml')
#selectors.save(selectors, 'C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SelectorsPage.yml')


