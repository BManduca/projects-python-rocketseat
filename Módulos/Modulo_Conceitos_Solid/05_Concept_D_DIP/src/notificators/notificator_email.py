from drivers.interfaces.notificator_interface import NotificatorInterface

class EmailNotificationSender(NotificatorInterface):
  def send_notification(self, message: str) -> None:
    print(f'Sending Email: {message}')