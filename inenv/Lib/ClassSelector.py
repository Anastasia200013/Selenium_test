from typing import List

import yaml

from inenv.Lib.ClassAbonent import Abonent
import inspect


class Location:
    field_name: str
    location: str

    def __init__(self, field_name: str, location: str) -> None:
        self.field_name = field_name
        self.location = location

    def __repr__(self):
        return f"field_name:{self.field_name}, location:{self.location}"


class Selectors:
    file_test: str
    type: str
    locations: List[Location]

    def __init__(self, file_test: str, type: str, locations: List[Location]) -> None:
        self.file_test = file_test
        self.type = type
        self.locations = locations

    @staticmethod
    def generate():
        obj = Selectors('', Abonent.__name__, [Location(field_name, "")
                                               for field_name in list(Abonent.__dict__["__annotations__"].keys())])
        return obj

    def save(self, path):
        with open(path, "w") as f:
            yaml.dump(self, f)

    @staticmethod
    def load(path):
        with open(path, "r") as f:
            return yaml.load(f, yaml.Loader)
        # print(obj.file_test, obj.type, obj.locations)
        # print(objab.__class.__name__)
#selectors = Selectors.generate()
#selectors.save('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SearchSelectors222.yml')
# print(selectors.__dict__)
# selectors2 = Selectors.load('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SearchSelectors222.yml')
# print(selectors2.__dict__)
