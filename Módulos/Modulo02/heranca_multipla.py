from modules.styleModule import jumpLine, printTextCentralized, imprimirLinha
from os import system
import time

class Animal:
    def __init__(self,nome) -> None:
        self.name = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        jumpLine()
        return f'{self.name} está amamentando.'

class Ave(Animal):
    def voar(self):
        jumpLine()
        return f'{self.name} está voando.'

class Morcego(Mamifero, Ave):
    def emitir_som(self):
        jumpLine()
        return 'Morcegos emitem sons ultrassônicos.'

morcego = Morcego('Batman')

# acessando os métodos da classe base 'Animal'
jumpLine()
imprimirLinha(2,20)
printTextCentralized(f'NOME DO MORCEGO: {morcego.name}.',60,2)
printTextCentralized(f'SOM: {morcego.emitir_som().upper()}',60,2)

# acessando métodos das classes 'Mamíferos' e 'Aves'
printTextCentralized(f'{morcego.amamentar().upper()}',60,2)
printTextCentralized(f'{morcego.voar().upper()}',60,2)
imprimirLinha(2,20)
