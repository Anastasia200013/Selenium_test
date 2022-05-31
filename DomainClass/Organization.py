from datetime import date
from DomainClass.House import House
from DomainClass.Service import Service
from typing import List


class Organization:
    contractor_id: str
    contractor_name: str
    amount_accountcd: int
    amount_houses: int
    amount_services: int
    accrued_on_month: str
    accrued_on_closet_until_month: date
    information_owner: bool
    services: List[Service]
    houses: List[House]

    def __init__(self, contractor_id: str, contractor_name: str, amount_accountcd: int, amount_houses: int,
                 amount_services: int, accrued_on_month: date, accrued_on_closet_until_month: date,
                 information_owner: bool, services: List[Service], houses: List[House]) -> None:
        self.contractor_id = contractor_id
        self.contractor_name = contractor_name
        self.amount_accountcd = amount_accountcd
        self.amount_houses = amount_houses
        self.amount_services = amount_services
        self.accrued_on_month = accrued_on_month
        self.accrued_on_closet_until_month = accrued_on_closet_until_month
        self.information_owner = information_owner
        self.services = services
        self.houses = houses
