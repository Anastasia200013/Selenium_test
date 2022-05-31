from DomainClass.Parameter import Parameter
from DomainClass.Characteristic import Characteristic
from DomainClass.Organization import Organization
from DomainClass.Counter import Counter
from typing import List


class Abonent:
    accountcd: str
    fio: str
    phone_number: str
    address: str
    contractor_information: str
    characteristics: List[Characteristic]
    parameters: List[Parameter]
    organizations: List[Organization]
    counters: List[Counter]

    def __init__(self, accountcd: str, fio: str, phone_number: str, address: str, contractor_information: str,
                 characteristics: List[Characteristic], parameters: List[Parameter], organizations: List[Organization],
                 counters: List[Counter]) -> None:
        self.accountcd = accountcd
        self.fio = fio
        self.phone_number = phone_number
        self.address = address
        self.contractor_information = contractor_information
        self.characteristics = characteristics
        self.parameters = parameters
        self.organizations = organizations
        self.counters = counters
