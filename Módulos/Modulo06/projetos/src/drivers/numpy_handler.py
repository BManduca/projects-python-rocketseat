import numpy
from typing import List
from .interfaces.driver_handler_interface import DriverHandlerInterface

class NumpyHandler(DriverHandlerInterface):
    def __init__(self) -> None:
        self.__np = numpy

    # calc standard deviation
    def standard_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)
    
    # calc variance
    def variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)
