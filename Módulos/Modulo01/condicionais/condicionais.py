# Condicionais => if, elif, else.

idade = int(input('Insira sua idade: '))
print(' ')
if idade >= 18:
    print('Maior de idade')
elif idade >= 12:
    print('Você é um adolescente')
else:
    print('Menor de idade')

mensagem = 'Pode tirar a carteira de habilitação' if idade >= 18 else 'Você não pode tirar a carteira de habilitação'
print(mensagem)