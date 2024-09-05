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

# criando um dicionário de exemplo
# pessoa = {}

# pessoa['nome'] = str(input('Insira o nome: '))
# pessoa['sobrenome'] = str(input('Insira o sobrenome: '))
# pessoa['idade'] = int(input('Insira a idade: '))
# pessoa['cidade'] = str(input('Insira a cidade: '))

pessoa = {'nome': 'Brunno', 'sobrenome': 'Manduca', 'idade': 32, 'cidade': 'Florianópolis'}

print(' ')
imprimirLinha20(2)
for c, v in pessoa.items():
    printTextCentralized(f'{c.capitalize()} => {v}', 60, 2)
    # print(f'{c} => {v}')
imprimirLinha20(2)

# cast em list, para pegar os elementos dentro da lista
chaves = list(pessoa.keys())
print(' ')
print('Chaves do meu dicionário:', chaves)
print('Primeira chave:', chaves[0])

valores = list(pessoa.values())
print(' ')
print('Valores do meu dicionário:', valores)
print('Primeiro valor:', valores[0])

items = list(pessoa.items())
print(' ')
print('Items do meu dicionário:', items)
print('Primeiro item:', items[0])
print('Primeira chave-valor: %s = %s' % (items[0][0], items[0][1]))