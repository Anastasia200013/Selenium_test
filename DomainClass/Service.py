from DomainClass.Counter import Counter
from typing import List


class Service:
    serviceid: str
    service_name: str
    counters: List[Counter]

    def __init__(self, serviceid: str, service_name: str, counters: List[Counter]) -> None:
        self.serviceid = serviceid
        self.service_name = service_name
        self.counters = counters
