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

def main():
    while True:
        print(' ')
        imprimirLinha20(4)
        printTextCentralized('MENU DO GERENCIADOR DE LISTA DE TAREFAS', 60, 4)
        print(' ')
        printTextCentralized('1. ADICIONAR TAREFA', 60, 4)
        printTextCentralized('2. VER TAREFAS', 60, 4)
        printTextCentralized('3. ATUALIZAR TAREFA', 60, 4)
        printTextCentralized('4. COMPLETAR TAREFA', 60, 4)
        printTextCentralized('5. DELETAR TAREFAS COMPLETADAS', 60, 4)
        printTextCentralized('6. SAIR', 60, 4)
        imprimirLinha20(4)

        choice = input('\nINSIRA A OPÇÃO DESEJADA: ')

        print(' ')

        if choice == '6':
            print(' ')
            imprimirLinha20(3)
            printTextCentralized('FINALIZANDO PROGRAMA...', 60, 3)
            imprimirLinha20(3)
            time.sleep(2)
            break


if __name__ == "__main__":
    main()
