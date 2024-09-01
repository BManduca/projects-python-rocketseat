from src.calculators.calculator04 import Calculator4
from src.drivers.numpy_handler import NumpyHandler

def calculator04_factory():
  numpy_handler = NumpyHandler()
  calc = Calculator4(numpy_handler)
  return calc