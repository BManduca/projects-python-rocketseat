from .calculator02 import Calculator2
from typing import Dict

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():

    mock_request = MockRequest(body={
        'numbers': [
            2.34,
            5.67,
            8.09
        ]
    })

    calculator02 = Calculator2()
    calculator02.calculate(mock_request)