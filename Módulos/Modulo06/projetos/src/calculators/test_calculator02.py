from .calculator02 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from typing import Dict, List
import numpy

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> None:
        return self.__np.std(numbers)

# teste Integração entre NumpyHandler e Calculator02
def test_calculate_integration():

    mock_request = MockRequest( body={ 'numbers': [ 2.34, 5.67, 8.09 ] } )
    
    driver = NumpyHandler()
    calculator02 = Calculator2(driver)
    formated_response = calculator02.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.05}}

def test_calculate():

    mock_request = MockRequest( body={ 'numbers': [ 2.12, 4.62, 1.32 ] } )
    
    # testing isolated behavior Calculator02
    driver = MockDriverHandler()
    calculator02 = Calculator2(driver)
    formated_response = calculator02.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.07}}

    
