from DomainClass.Abonent import Abonent
from inenv.Lib.Case import TestDescription
from inenv.Lib.Selector import Selectors
from inenv.Lib.SQLWrapper import SQLWrapper
from DomainClass.Organization import Organization
from inenv.Lib.RegexWrapper import RegexWrapper
from DomainClass.Counter import Counter

if __name__ == '__main__':
      selectors = Selectors.generate(Abonent)
    # selectors.save('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SelectorsAbonent.yml')
    # suit = TestDescription.generate('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SelectorsAbonent.yml', Abonent)
    # suit.save(suit, 'C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\TestCases\\TestsAbonent.yml')
    # RegexWrapper.generate_test_regex_script(Abonent, "TestRegexAbonent", "C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\MainTesting\\Test_Data_RegexAbonent.py")
    #
    # selectors = Selectors.generate(Organization)
    # selectors.save('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SelectorsOrganization.yml')
    # suit = TestDescription.generate('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SelectorsOrganization.yml', Organization)
    # suit.save(suit, 'C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\TestCases\\TestsOrganization.yml')
    # SQLWrapper.generate_test_request_script(Organization, "TestRegexOrganization","C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\MainTesting\\Test_Data_SQLOrganization.py")
    # RegexWrapper.generate_test_regex_script(Organization, "TestRegexOrganization","C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\MainTesting\\Test_Data_RegexOrganization.py")
    #
    # selectors = Selectors.generate(Counter)
    # selectors.save('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SelectorsCounter.yml')
    # suit = TestDescription.generate('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SelectorsCounter.yml', Counter)
    # suit.save(suit, 'C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\TestCases\\TestsCounter.yml')
    # SQLWrapper.generate_test_request_script(Counter, "TestRegexOrganization","C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\MainTesting\\Test_Data_SQLCounter.py")
    # RegexWrapper.generate_test_regex_script(Counter, "TestRegexOrganization","C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\MainTesting\\Test_Data_RegexCounter.py")


