from modules.styleModule import jumpLine, printTextCentralized, imprimirLinha
from os import system
from abc import ABC, abstractmethod
import time

jumpLine()
imprimirLinha(2,20)
printTextCentralized('EXEMPLO DE ABSTRAÇÃO', 60, 2)
imprimirLinha(2,20)

class Veiculo(ABC):
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        jumpLine()
        imprimirLinha(4,20)
        printTextCentralized('CARRO LIGADO USANDO A CHAVE',60,4)
        imprimirLinha(4,20)

    def desligar(self):
        jumpLine()
        imprimirLinha(3,20)
        printTextCentralized('CARRO DESLIGADO USANDO A CHAVE',60,3)
        imprimirLinha(3,20)

carro_amarelo = Carro()
carro_amarelo.ligar()
carro_amarelo.desligar()
time.sleep(5)
system('clear')