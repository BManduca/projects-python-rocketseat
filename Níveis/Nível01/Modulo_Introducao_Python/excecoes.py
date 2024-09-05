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
imprimirLinha(4,22)
printTextCentralized('EXEMPLO DE CAPTURA DE EXCEÇÕES.',60,4)
imprimirLinha(4,22)

try:
    jumpLine()
    number = int(input('INSIRA UM NÚMERO INTEIRO: '))
    result = 10/number
except ValueError as ve:
    jumpLine()
    imprimirLinha(1,30)
    printTextCentralized(f'Exception value error: {ve}.',90,1)
    imprimirLinha(1,30)
    # raise ValueError('Tipo de variáveis incompatíveis')
except Exception as excp:
    jumpLine()
    imprimirLinha(1,22)
    printTextCentralized(f'Erro: {excp}',60,1)
    imprimirLinha(1,22)
else:
    print(f'Resultado da operação: {result:.2f}')
finally:
    jumpLine()
    imprimirLinha(2,20)
    printTextCentralized('Operação finalizada!', 60, 2)
    imprimirLinha(2,20)
