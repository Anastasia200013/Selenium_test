from datetime import date


class Counter:
    serviceid: str
    mark: str
    counter_name: str
    serial_number: str
    registration_date: date
    installation_location: str
    status: str
    indications_now: int
    initial_indications: int
    next_verification_date: date
    last_verification_date: date
    date_seal: date
    number_seal: str
    type_seal: str
    regime: str

    def __init__(self, serviceid: str, counterid: str, mark: str, counter_name: str, serial_number: str,
                 registration_date: date, installation_location: str, status: str, indications_now: int,
                 initial_indications: int, next_verification_date: date, last_verification_date: date, date_seal: date,
                 number_seal: str, type_seal: str, regime: str) -> None:
        self.serviceid = serviceid
        self.counterid = counterid
        self.mark = mark
        self.counter_name = counter_name
        self.serial_number = serial_number
        self.registration_date = registration_date
        self.installation_location = installation_location
        self.status = status
        self.indications_now = indications_now
        self.initial_indications = initial_indications
        self.next_verification_date = next_verification_date
        self.last_verification_date = last_verification_date
        self.date_seal = date_seal
        self.number_seal = number_seal
        self.type_seal = type_seal
        self.regime = regime
