from datetime import date


class Characteristic:
    type_informtion: str
    characteristic_id: str
    name: str
    present_value: int
    date_of_change: date
    value: str
    valid_from: date
    valid_for: date
    account_date: date
    start_date: date
    edit: bool

    def __init__(self, type_informtion: str, characteristic_id: str, name: str, present_value: int,
                 date_of_change: date, value: str, valid_from: date, valid_for: date, account_date: date,
                 start_date: date, edit: bool) -> None:
        self.type_informtion = type_informtion
        self.characteristic_id = characteristic_id
        self.name = name
        self.present_value = present_value
        self.date_of_change = date_of_change
        self.value = value
        self.valid_from = valid_from
        self.valid_for = valid_for
        self.account_date = account_date
        self.start_date = start_date
        self.edit = edit
        