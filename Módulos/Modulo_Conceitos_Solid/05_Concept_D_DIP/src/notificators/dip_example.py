from src.drivers.interfaces.notificator_interface import NotificatorInterface
from .notificator_sms import SMSNotificationSender
from .notificator_email import EmailNotificationSender

# módulo de alto nível
class ClientService:
  def __init__(self, notificator: NotificatorInterface) -> None:
    # atributo da nossa classe
    self.notificator = notificator

  def send(self, message: str) -> None:
    self.notificator.send_notification(message)

obj = ClientService(SMSNotificationSender)
obj.send('Hello, World!')