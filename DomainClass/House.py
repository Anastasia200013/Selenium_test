from typing import List
from DomainClass.Service import Service


class House:
    houseid: str
    address: str
    type: str
    amount_counters: int
    amount_accountcd: int
    amount_apartmentes: int
    amount_of_registered: int
    area_house: int
    services: List[Service]

    def __init__(self, houseid: str, address: str, type: str, amount_counters: int, amount_accountcd: int,
                 amount_apartmentes: int, amount_of_registered: int, area_house: int, services: List[Service]) -> None:
        self.houseid = houseid
        self.address = address
        self.type = type
        self.amount_counters = amount_counters
        self.amount_accountcd = amount_accountcd
        self.amount_apartmentes = amount_apartmentes
        self.amount_of_registered = amount_of_registered
        self.area_house = area_house
        self.services = services
