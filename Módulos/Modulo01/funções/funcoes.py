# FUNÇÕES

def saudacao(nome):
    print(f'Olá, {nome}!')

print('\nChamando função saudação: ')
saudacao('Maria')
saudacao('Brunno')


def quadrado(num):
    result = num ** 2
    return result

def soma(num1, num2):
    result = num1 + num2
    return result

print(' ')
valor = 2
valor_quadrado = quadrado(valor)
print(f'o {valor} elevado ao quadrado é: {valor_quadrado}')

print(' ')
valor1 = 10
valor2 = 13
valor_soma = soma(valor1, valor2)
print(f'A soma de {valor1} e {valor2} é: {valor_soma}')