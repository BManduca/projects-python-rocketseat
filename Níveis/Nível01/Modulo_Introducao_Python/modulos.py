import math

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

jumpLine()
imprimirLinha(2,20)
printTextCentralized('EXEMPLO DE IMPORTAÇÃO DE UM MÓDULO PADRÃO',60,2)
imprimirLinha(2,20)

jumpLine()
valor_calc_raiz = int(input('INSIRA UM VALOR, PARA CALCULAR SUA RAIZ QUADRADA: '))
raiz_quadrada = math.sqrt(valor_calc_raiz)
jumpLine()

imprimirLinha(4,20)
printTextCentralized(f'A RAIZ QUADRADA DE {valor_calc_raiz} É: {raiz_quadrada}',60,4)
imprimirLinha(4,20)

jumpLine()
imprimirLinha(2,20)
printTextCentralized('EXEMPLO DE CRIAÇÃO E UTILIZAÇÃO DE UM MÓDULO PERSONALIZADO',60,2)
imprimirLinha(2,20)

import styleTextModule

styleTextModule.jumpLine()
styleTextModule.imprimirLinha(2,20)
styleTextModule.printTextCentralized('Testando importação de módulo personalizado',60,2)
styleTextModule.imprimirLinha(2,20)