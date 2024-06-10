import time
from os import system

# INICIANDO O PROJETO

colors = (
    '\033[0m', # 0 - SEM COR
    '\033[0;31m', # 1 - VERMELHO
    '\033[0;32m', # 2 - VERDE
    '\033[0;33m', # 3 - AMARELO
    '\033[0;34m', # 4 - AZUL
    '\033[0;35m', # 5 - ROXO
    '\033[0;36m', # 6 - BRANCO
)

def jumpLine():
    print('\n')

def messageCentralized(msg, wid):
    tam = len(msg)
    space = (wid - tam) // 2
    text = ' ' * space + msg + ' ' * space
    # Se o texto não puder ser centralizado perfeitamente, ajuste uma posição para a direita
    if len(text) < wid:
        text += ' '
        
    return text

def printTextCentralized(msg, wid, cor=0):
    message = messageCentralized(msg, wid)
    print(colors[cor], end='')
    print(message)
    print(colors[0], end='')

def imprimirLinha20(cor=0):
    print(colors[cor], end='')
    print('-=-'*20)
    print(colors[0], end='')

def imprimirLinha30(cor=0):
    print(colors[cor], end='')
    print('-=-'*30)
    print(colors[0], end='')

def add_task(lista_tarefas, name_task):
    """
        estrutura da tarefa:
        - tarefa: nome da tarefa
        - completada: indicar se a tarefa foi completada ou não
    """
    tarefa = {'tarefa': name_task, 'completada': False}
    lista_tarefas.append(tarefa)
    jumpLine()
    imprimirLinha30(2)
    printTextCentralized(f'Tarefa {name_task} foi adicionada com sucesso!', 80, 2)
    imprimirLinha30(2)
    jumpLine()
    time.sleep(4)
    system('clear')
    return

def view_tasks(lista_tarefas):
    jumpLine()
    imprimirLinha20(4)
    printTextCentralized('LISTA DE TAREFAS: ', 60, 4)
    for index, tarefa in enumerate(lista_tarefas, start=1):
        """
            status = '✓' if tarefa['completada'] else ' '

            ou 

            if tarefa['completada']:
                status = '✓'
            else:
                status = ' '
        """
        status = '✓' if tarefa['completada'] else ' '
        nome_tarefa = tarefa['tarefa']
        printTextCentralized(f'{index}. [{status}] {nome_tarefa}', 60, 4)
    imprimirLinha20(4)
    time.sleep(7)
    system('clear')


tarefas = []

def showMenu():
    jumpLine()
    imprimirLinha20(4)
    printTextCentralized('MENU DO GERENCIADOR DE LISTA DE TAREFAS', 60, 4)
    jumpLine()
    printTextCentralized('1. ADICIONAR TAREFA', 60, 4)
    printTextCentralized('2. VER TAREFAS', 60, 4)
    printTextCentralized('3. ATUALIZAR TAREFA', 60, 4)
    printTextCentralized('4. COMPLETAR TAREFA', 60, 4)
    printTextCentralized('5. DELETAR TAREFAS COMPLETADAS', 60, 4)
    printTextCentralized('6. SAIR', 60, 4)
    imprimirLinha20(4)


def main():
    while True:
        showMenu()
        jumpLine()

        textChoice = '\nINSIRA A OPÇÃO DESEJADA: '
        choice = input(f'{textChoice}')

        jumpLine()

        if choice == '1':
            nome_tarefa = input('Insira o nome da tarefa que desejar adicionar: ')
            add_task(tarefas, nome_tarefa)
        elif choice == '2':
            view_tasks(tarefas)
        elif choice == '6':
            jumpLine()
            imprimirLinha20(3)
            printTextCentralized('FINALIZANDO PROGRAMA...', 60, 3)
            imprimirLinha20(3)
            jumpLine()
            time.sleep(2)
            system('clear')
            break
        else:
            jumpLine()
            imprimirLinha20(1)
            printTextCentralized('OPÇÃO INVÁLIDA!',60,1)
            printTextCentralized('POR FAVOR INSIRA NOVAMENTE UMA OPÇÀO DO MENU!', 60, 1)
            imprimirLinha20(1)
            time.sleep(5)
            system('clear')


if __name__ == "__main__":
    main()
