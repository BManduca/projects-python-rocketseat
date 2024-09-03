
from drivers.interfaces.notificator_interface import NotificatorInterface

class SMSNotificationSender(NotificatorInterface):
  def send_notification(self, message: str) -> None:
    print(f'Sending SMS: {message}')