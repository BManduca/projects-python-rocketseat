from modules.styleModule import jumpLine, printTextCentralized, imprimirLinha

class Pessoa:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def saudacao(self):
        return f'Bom Dia, meu nome é {self.name} e eu tenho {self.age} anos.'

pessoa1 = Pessoa('Brunno',32)
jumpLine()
imprimirLinha(2,20)
printTextCentralized(f'Nome: {pessoa1.name} | Idade: {pessoa1.age} anos',60,2)
imprimirLinha(2,20)
jumpLine()
mensagem = pessoa1.saudacao()
imprimirLinha(4,20)
printTextCentralized(mensagem, 60,4)
imprimirLinha(4,20)
pessoa2 = Pessoa('João',28)
jumpLine()
imprimirLinha(2,20)
printTextCentralized(f'Nome: {pessoa2.name} | Idade: {pessoa2.age} anos',60,2)
imprimirLinha(2,20)
jumpLine()
mensagem2 = pessoa2.saudacao()
imprimirLinha(4,20)
printTextCentralized(mensagem2, 60,4)
imprimirLinha(4,20)