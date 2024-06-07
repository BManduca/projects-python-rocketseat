# uso do for

lista = [1, 2, 3, 4, 5, 6]

print('\nLISTA')
for element in lista:
    print(f'{element}')

print('\nTUPLA')
tupla = (1, 2, 3, 4, 5, 6)
for element in tupla:
    print(f'{element}')

print('\nDICIONÁRIO')
pessoa = {'nome': 'Brunno', 'sobrenome': 'Manduca', 'idade': 32, 'cidade': 'Florianópolis'}

print('\nUSO DO FOR APRESENTANDO AS CHAVES DE UM DICIONÁRIO')
for key in pessoa.keys():
    print(f'{key}')

print('\nUSO DO FOR APRESENTANDO OS VALORES DE UM DICIONÁRIO')
for element in pessoa.values():
    print(f'{element}')

print('\nUSO DO FOR APRESENTANDO A CHAVE-VALOR DE UM DICIONÁRIO')
for key, element in pessoa.items():
    print(f'{key} => {element}')

print('\nUSO DA FUNÇÃO RANGE()')
for element in range(5):
    print(element)

print('\nUSO DA FUNÇÃO RANGE() COM LEN()')
for element in range(0, len(lista)):
    print(f'Elemento {element} => {lista[element]}')

print('\nUSO DA FUNÇÃO ENUMERATE()')
lista_enumerate = ['a', 'b', 'c']
for indice, valor in enumerate(lista_enumerate):
    print(f'{indice} => {valor}')
    if indice == 1:
        print('INDICE 1')