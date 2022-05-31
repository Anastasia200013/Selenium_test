from typing import List


class Element:
    name_element: str
    action: str

    def __init__(self, name_element: str, action: str) -> None:
        self.name_element = name_element
        self.action = action


class Page:
    name_page: str
    elements: List[Element]

    def __init__(self, name_page: str, elements: List[Element]) -> None:
        self.name_page = name_page
        self.elements = elements
