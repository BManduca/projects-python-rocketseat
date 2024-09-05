from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator03 import Calculator3

def calculator03_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator3(numpy_handler)
    return calc