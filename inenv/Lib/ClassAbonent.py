class Abonent(object):
    accountcd: str
    fio: str
    phone_number: str
    address: str
    accountcd_kvc: str
    contractor_information: str
    services: str
    counters: str

    def __init__(self, accountcd: str = None, fio: str = None, phone_number: str = None, address: str = None,
                 accountcd_kvc: str = None, contractor_information: str = None, services: str = None,
                 counters: str = None) -> None:
        self.accountcd = accountcd
        self.fio = fio
        self.phone_number = phone_number
        self.address = address
        self.accountcd_kvc = accountcd_kvc
        self.contractor_information = contractor_information
        self.services = services
        self.counters = counters


# abon0 = Abonent('string', 'string', 'string', 'string', 'string', 'string', 'string', 'string')
abon1 = Abonent()
# print(abon0.__dict__)
print(list(abon1.__dict__.keys()))
print(list(Abonent.__dict__.keys()))
print(list(Abonent.__dict__["__annotations__"].keys()))
