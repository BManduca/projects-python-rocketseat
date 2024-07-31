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
    formated_response = calculator02.calculate(mock_request)
    print()
    print(formated_response)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.05}}

    
