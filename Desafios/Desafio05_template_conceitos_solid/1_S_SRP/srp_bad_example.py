'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''

def printLine():
    print('-=-' * 20)

def printMessage(msg):
    print(f'{msg:^60}')

class TaskHandler:

    def handle(self):
        self.__conect_api()
        self.__create_task()
        self.__update_task()
        self.__remove_task()
        self.__send_notification()
        self.__generate_report()
        self.__send_report()

    # separate connect api
    def __conect_api(self):
        printMessage('Realizando a conexão com a API...')


    # separate task creation
    def __create_task(self):
        printMessage('Realizando a criação de uma task...')


    # separate task update
    def __update_task(self):
        printMessage('Realizando a atualização de uma task...')

    def __remove_task(self):
        printMessage('Realizando a remoção de uma task...')

    def __send_notification(self):
        printMessage('Realizando o envio de uma notificação...')

    def __generate_report(self):
        printMessage('Gerando um report...')

    def __send_report(self):
        printMessage('Realindo o envio do report...')

taskhandler = TaskHandler()
printLine()
taskhandler.handle()
printLine()