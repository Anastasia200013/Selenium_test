from inenv.Lib.ClassAbonent import Abonent
from inenv.Lib.ClassSelector import Selectors
from inenv.Lib.Utility import generate_test_script

selectors = Selectors.generate()

if __name__ == '__main__':
    generate_test_script(Abonent, "C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\MainTesting\\Test_Data_Regex.py")
    selectors.save('C:\\Users\\a.petrova\\PycharmProjects\\selenium-test\\SearchSelect\\SearchSelectors21.yml')
