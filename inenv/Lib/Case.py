from typing import List
import yaml
from inenv.Lib.Selector import Selectors
from inenv.Lib.Serialization import Serialization
from DomainClass.Organization import Organization
from DomainClass.Counter import Counter


class Test:
    statement: str
    type: str
    test_source: str
    exp: str

    def __init__(self, statement: str, type: str, test_source: str, exp: str) -> None:
        self.statement = statement
        self.type = type
        self.test_source = test_source
        self.exp = exp

    def __repr__(self):
        return f"statement:{self.statement}, type:{self.type}, test_source:{self.test_source}, exp:{self.exp}"

    @staticmethod
    def find_by_statement(cases, statement):
        for case in cases:
            if case.statement == statement:
                return case


class TestDescription(Serialization):
    test: str
    file_abonent: str
    tests: List[Test]

    def __init__(self, test: str, file_abonent: str, tests: List[Test]) -> None:
        self.test = test
        self.file_abonent = file_abonent
        self.tests = tests

    @staticmethod
    def generate(path_searchselect, some_class):
        selector = Selectors.load(path_searchselect)
        obj = TestDescription('', '',  [Test((f"FOR {selector.type}.{field_test_name}"), "", "", "")
                                            for field_test_name in list(some_class.__dict__["__annotations__"].keys())])
        return obj



#suit = TestDescription.generate('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SelectorsOrganization.yml', Organization)
#suit.save(suit, 'C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\TestCases\\TestsOrganization.yml')
#suit = TestDescription.generate('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SelectorsCounter.yml', Counter)
#suit.save(suit, 'C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\TestCases\\TestsCounter.yml')

