from .interfaces.driver_handler_interface import DriverHandlerInterface
from typing import List
import numpy as np

class NumpyHandler(DriverHandlerInterface):

  def __init__(self) -> None:
    self.__np = np

  # calc average
  def average(self, numbers: List[float]) -> float:
    return self.__np.average(numbers)