from .calculator03 import Calculator3
from pytest import raises
from typing import Dict, List
import numpy

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

# class MockDriverHandlerError:

#     def __init__(self) -> None:
#         self.__np = numpy

#     def variance(self, numbers: List[float]) -> float:
#         return self.__np.var(numbers)

class MockDriverHandlerError:

    def variance(self, numbers: List[float]) -> float:
        return 3
    
class MockDriverHandler:

    def variance(self, numbers: List[float]) -> float:
        return 1000000


def test_calculate_with_variance_error():
    mock_request = MockRequest({ "numbers": [ 1, 2, 3, 4, 5 ] })
    calculator03 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as except_info:
        calculator03.calculate(mock_request)

    assert str(except_info.value) == 'Falha no processo: Variância é menor que a multiplicação!'

def test_calculate():
    mock_request = MockRequest({ "numbers": [ 1, 1, 1, 1, 100 ] })
    calculator03 = Calculator3(MockDriverHandler())
    
    response = calculator03.calculate(mock_request)

    assert response == {'data': {'Calculator': 3, 'value': 1000000, 'success': True}}