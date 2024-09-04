from abc import ABC, abstractmethod

class NotificatorInterface(ABC):

  @abstractmethod
  def send_notification(self, message: str) -> None:
    pass

  
class EmailNotificationSender(NotificatorInterface):
  def send_notification(self, message: str) -> None:
    print(f'Sending Email: {message}')

class SMSNotificationSender(NotificatorInterface):
  def send_notification(self, message: str) -> None:
    print(f'Sending SMS: {message}')

# módulo de alto nível
class ClientService:
  def __init__(self, notificator: NotificatorInterface) -> None:
    # atributo da nossa classe
    self.__notificator = notificator

  def send(self, message: str) -> None:
    self.__notificator.send_notification(message)

obj = ClientService(EmailNotificationSender())
obj.send('Hello, World!')