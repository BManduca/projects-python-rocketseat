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

print(' ')
idade = int(input('Insira sua idade: '))

def main():
    if idade < 18:
        print(' ')
        imprimirLinha20(3)
        printTextCentralized('Usuário é menor de idade', 60, 3)
        imprimirLinha20(3)
    else:
        print(' ')
        imprimirLinha20(2)
        printTextCentralized('Usuário maior de idade', 60, 2)
        imprimirLinha20(2)


if __name__ == '__main__':
    main()