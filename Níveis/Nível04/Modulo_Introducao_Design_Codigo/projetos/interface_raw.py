from abc import ABC, abstractmethod

'''
    função de definir a regra de construção das 
    demais classes que ela é implementada.
'''

class NotificationSender(ABC):

    @abstractmethod
    def send_notification(self, message: str) -> None:
        pass

class EmailNotificationSender(NotificationSender):

    def send_notification(self, message: str) -> None:
        print(f'EMAIL MESSAGE - {message}')

class SMSNotificationSender(NotificationSender):

    def send_notification(self, message: str) -> None:
        print(f'SMS MESSAGE - {message}')

class Notificator:
    def __init__(self, notification_sender: NotificationSender) -> None:
        self.__notification_sender = notification_sender

    def send(self, message: str) -> None:
        # realizar validacao de dados
        self.__notification_sender.send_notification(message)

# obj = EmailNotificationSender()
# obj.send_notification('Olá Mundo!')

obj = Notificator(EmailNotificationSender())
obj.send('Olá Mundo')