from src.calculators.calculator02 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

def calculator02_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator2(numpy_handler)
    return calc