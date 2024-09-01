from src.drivers.numpy_handler import NumpyHandler
from .calculator04 import Calculator4
from typing import Dict, List
import numpy

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandler:
  def __init__(self) -> None:
    self.__np = numpy

  def average(self, numbers: List[float]) -> None:
    return self.__np.average(numbers)


# teste de integração entre NumpyHandler 
# definido nos drivers e a Calculator04
def test_calculate_integration():

  mock_request = MockRequest(
    body = {
      'numbers': [
        1.45,
        2.67,
        8.76,
        9.45,
        0.76
      ]
    }
  )

  driver = NumpyHandler()
  calculator04 = Calculator4(driver)
  formatted_response = calculator04.calculate(mock_request)

  assert isinstance(formatted_response, dict)
  assert formatted_response == {
    'data': {
      'Calculator': 4,
      'average': 4.62
    }
  }

def test_calculate():

  mock_request = MockRequest(
    body = {
      'numbers': [
        4.56,
        6.54,
        3.24,
        0.98,
        3.66
      ]
    }
  )

  #testing isolated behavior Calculator04
  # driver = MockDriverHandler()
  calculator04 = Calculator4(MockDriverHandler())
  formatted_response = calculator04.calculate(mock_request)

  assert isinstance(formatted_response, dict)
  assert formatted_response == {
    'data': {
      'Calculator': 4,
      'average': 3.8
    }
  }

