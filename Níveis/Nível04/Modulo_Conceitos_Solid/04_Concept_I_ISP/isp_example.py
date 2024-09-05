from abc import ABC, abstractmethod

#  interface genérica -> quebra o principio de segregação de interfaces
class Document(ABC): # GENERIC

  @abstractmethod
  def load(self): pass

  @abstractmethod
  def view(self): pass

  @abstractmethod
  def format(self): pass

  @abstractmethod
  def calculate(self): pass
  
class DocumentPDF(ABC): # ISP
  @abstractmethod
  def load(self): pass

  @abstractmethod
  def view(self): pass

class DocumentTXT(ABC): # ISP
  @abstractmethod
  def load(self): pass

  @abstractmethod
  def format(self): pass

class DocumentExcel(ABC): # ISP
  @abstractmethod
  def load(self): pass

  @abstractmethod
  def calculate(self): pass