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

def imprimirLinha(cor=0, wid=0):
    print(colors[cor], end='')
    print('-=-'*wid)
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
    imprimirLinha(2,30)
    printTextCentralized(f'Tarefa {name_task} foi adicionada com sucesso!', 80, 2)
    imprimirLinha(2,30)
    jumpLine()
    time.sleep(4)
    system('clear')
    return

def view_tasks(lista_tarefas):
    jumpLine()
    imprimirLinha(4,26)
    printTextCentralized('LISTA DE TAREFAS: ', 70, 4)
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
        printTextCentralized(f'{index}. [{status}] {nome_tarefa}', 70, 4)
    imprimirLinha(4,26)
    jumpLine()
    time.sleep(4)
    system('clear')
    return

def view_tasks_v2(lista_tarefas):
    jumpLine()
    imprimirLinha(4,26)
    printTextCentralized('LISTA DE TAREFAS: ', 66, 4)
    for index, tarefa in enumerate(lista_tarefas, start=1):
        status = '✓' if tarefa['completada'] else ' '
        nome_tarefa = tarefa['tarefa']
        printTextCentralized(f'{index}. [{status}] {nome_tarefa}', 66, 4)
    imprimirLinha(4,26)
    jumpLine()
    return

def update_name_task(lista_tarefas, index_task, new_name_task):
    """
        como o index inicia em zero, precisamos passar o
        valor decrementado, para não ocorrer erro
    """
    index_task_adjust = int(index_task) - 1
    if len(lista_tarefas) > index_task_adjust >= 0:
        lista_tarefas[index_task_adjust]['tarefa'] = new_name_task
        jumpLine()
        imprimirLinha(5,30)
        printTextCentralized(f'Tarefa {index_task} atualizada para {new_name_task}.', 70, 5)
        imprimirLinha(5,30)
        time.sleep(5)
        system('clear')
    else:
        jumpLine()
        imprimirLinha(1,20)
        printTextCentralized('ÍNDICE DE TAREFA INVÁLIDO',60,1)
        printTextCentralized('FAVOR INSERIR UM ÍNDICE DE TAREFA VÁLIDO!',60,1)
        imprimirLinha(1,20)
        jumpLine()
        time.sleep(5)
        system('clear')
    return

def complete_task(lista_tarefas, index_task):
    index_task_to_complete = int(index_task) - 1

    if len(lista_tarefas) > index_task_to_complete >= 0:
        lista_tarefas[index_task_to_complete]['completada'] = True
        jumpLine()
        imprimirLinha(2,20)
        printTextCentralized(f'TAREFA {index_task} FOI MARCADA COMO COMPLETADA',60,2)
        imprimirLinha(2,20)
        jumpLine()
        time.sleep(5)
        system('clear')
    else:
        jumpLine()
        imprimirLinha(1,20)
        printTextCentralized('ÍNDICE DE TAREFA INVÁLIDO',60,1)
        printTextCentralized('FAVOR INSERIR UM ÍNDICE DE TAREFA VÁLIDO!',60,1)
        imprimirLinha(1,20)
        jumpLine()
        time.sleep(5)
        system('clear')
    return

def delete_complete_tasks(lista_tarefas):
    imprimirLinha(3,26)
    for tarefa in lista_tarefas:
        if tarefa['completada']:
            tarefas.remove(tarefa)
    printTextCentralized('TAREFAS COMPLETADAS FORAM DELETADAS COM SUCESSO.',70,3)
    imprimirLinha(3,26)
    return

tarefas = []

def showMenu():
    jumpLine()
    imprimirLinha(4,20)
    printTextCentralized('MENU DO GERENCIADOR DE LISTA DE TAREFAS', 60, 4)
    jumpLine()
    printTextCentralized('1. ADICIONAR TAREFA', 60, 4)
    printTextCentralized('2. VER TAREFAS', 60, 4)
    printTextCentralized('3. ATUALIZAR TAREFA', 60, 4)
    printTextCentralized('4. COMPLETAR TAREFA', 60, 4)
    printTextCentralized('5. DELETAR TAREFAS COMPLETADAS', 60, 4)
    printTextCentralized('6. SAIR', 60, 4)
    imprimirLinha(4,20)


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
        elif choice == '3':
            view_tasks_v2(tarefas)
            index_task = input('INSIRA O NÚMERO DA TAREFA QUE SERÁ ATUALIZADA: ')
            new_name_task = input('INSIRA O NOVO NOME DA TAREFA: ')
            update_name_task(tarefas, index_task, new_name_task)
        elif choice == '4':
            view_tasks_v2(tarefas)
            index_task = input('INSIRA O NÚMERO DA TAREFA QUE DESEJA COMPLETAR: ')
            complete_task(tarefas, index_task)
        elif choice == '5':
            delete_complete_tasks(tarefas)
            view_tasks(tarefas)
        elif choice == '6':
            jumpLine()
            imprimirLinha(3,20)
            printTextCentralized('FINALIZANDO PROGRAMA...', 60, 3)
            imprimirLinha(3,20)
            jumpLine()
            time.sleep(2)
            system('clear')
            break
        else:
            jumpLine()
            imprimirLinha(1,20)
            printTextCentralized('OPÇÃO INVÁLIDA!',60,1)
            printTextCentralized('POR FAVOR INSIRA NOVAMENTE UMA OPÇÀO DO MENU!', 60, 1)
            imprimirLinha(1,20)
            time.sleep(5)
            system('clear')


if __name__ == "__main__":
    main()
