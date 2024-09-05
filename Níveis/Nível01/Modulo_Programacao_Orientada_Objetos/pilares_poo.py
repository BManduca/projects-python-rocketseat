from modules.styleModule import jumpLine, printTextCentralized, imprimirLinha
from os import system
from abc import ABC, abstractmethod
import time

# HERANÇA E POLIMORFISMO
class Animal:
    def __init__(self,nome) -> None:
        self.name = nome

    def andar(self):
        imprimirLinha(3,20)
        printTextCentralized(f'O ANIMAL {self.name} ANDOU',60,3)
        imprimirLinha(3,20)
        return
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return 'AU AU'
    
class Gato(Animal):
    def emitir_som(self):
        return 'MIAU'
    
dog = Cachorro(nome='Rex')
cat = Gato(nome='Noah')

animals = [dog,cat]

jumpLine()
imprimirLinha(2,20)
printTextCentralized('EXEMPLO DE HERANÇA E POLIMORFISMO', 60, 2)
imprimirLinha(2,20)
jumpLine()
imprimirLinha(2,20)
for animal in animals:
    printTextCentralized(f'{animal.name} faz: {animal.emitir_som()}',60,2)
imprimirLinha(2,20)


jumpLine()
imprimirLinha(2,20)
printTextCentralized('EXEMPLO DE ENCAPSULAMENTO', 60, 2)
imprimirLinha(2,20)
jumpLine()

class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo # atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            jumpLine()
            imprimirLinha(2,20)
            printTextCentralized(f'DEPOSITO DE R$ {valor} REAIS REALIZADO COM SUCESSO',60,2)
            imprimirLinha(2,20)
        else:
            jumpLine()
            imprimirLinha(1,20)
            printTextCentralized(f'O VALOR {valor} INSERIDO PARA DEPÓSITO ESTA INCORRETO',60,1)
            imprimirLinha(1,20)
        return
        

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            jumpLine()
            imprimirLinha(2,20)
            printTextCentralized(f'SAQUE DE R$ {valor} REAIS REALIZADO COM SUCESSO',60,2)
            imprimirLinha(2,20)
        else:
            jumpLine()
            imprimirLinha(1,20)
            printTextCentralized(f'O VALOR {valor} INSERIDO PARA SAQUE ESTA INCORRETO.',60,1)
            imprimirLinha(1,20)
        return
        

    def consultar_saldo(self):
        return self.__saldo

def showMenu():
    jumpLine()
    imprimirLinha(4,20)
    printTextCentralized('MENU CONTA BANCÁRIA', 60, 4)
    jumpLine()
    printTextCentralized('1. VISUALIZAR SALDO', 60, 4)
    printTextCentralized('2. REALIZAR SAQUE', 60, 4)
    printTextCentralized('3. REALIZAR DEPÓSITO', 60, 4)
    printTextCentralized('4. FINALIZAR OPERAÇÃO', 60, 4)
    imprimirLinha(4,20)

def main():
    imprimirLinha(2,20)
    printTextCentralized('ACESSANDO CONTA BANCÁRIA',60,2)
    imprimirLinha(2,20)
    while True:
        showMenu()
        jumpLine()

        operationChoice = '\nINSIRA A OPÇÃO DESEJADA: '
        choice = input(f'{operationChoice}')

        jumpLine()

        if choice == '1':
            imprimirLinha(4,30)
            printTextCentralized(f'SALDO TOTAL DA CONTA É DE R$ {contaBrunno.consultar_saldo()} REAIS.',90,4)
            imprimirLinha(4,30)
            jumpLine()
            time.sleep(3)
            system('clear')
        elif choice == '2':
            saque = float(input('INSIRA O VALOR PARA REALIZAR O SAQUE: '))
            contaBrunno.sacar(saque)
            jumpLine()
            time.sleep(3)
            system('clear')
        elif choice == '3':
            deposito = float(input('INSIRA O VALOR QUE GOSTARIA DE DEPOSITAR: '))
            contaBrunno.depositar(deposito)
            jumpLine()
            time.sleep(3)
            system('clear')
        elif choice == '4':
            jumpLine()
            imprimirLinha(3,20)
            printTextCentralized('FINALIZANDO OPERAÇÃO...', 60, 3)
            imprimirLinha(3,20)
            jumpLine()
            time.sleep(2)
            system('clear')
            break
        else:
            jumpLine()
            imprimirLinha(1,20)
            printTextCentralized('OPÇÃO INVÁLIDA!',60,1)
            printTextCentralized('POR FAVOR INSIRA NOVAMENTE UMA OPÇÀO DO MENU!', 60, 1)
            imprimirLinha(1,20)
            time.sleep(5)
            system('clear')
        

    
contaBrunno = ContaBancaria(saldo=1000)

if __name__ == '__main__':
    main()

