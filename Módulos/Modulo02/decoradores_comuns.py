from modules.styleModule import jumpLine, printTextCentralized, imprimirLinha

'''
    aprendendo sobre decoradores comuns
        @classmethod
        @staticmethod
'''

class MinhaClasse:
    # atributo da classe
    valor = 10

    def __init__(self,nome) -> None:
        self.name = nome #Atributo da instancia

    # requer uma instancia para ser chamado.
    def metodo_instancia(self):
        imprimirLinha(4,20)
        printTextCentralized(f'MÉTODO DE INTÂNCIA CHAMADO PARA {self.name} COM {self.valor}',60,4)
        imprimirLinha(4,20)

    @classmethod
    def metodo_class(cls):
        printTextCentralized(f'MÉTODO DE CLASSE CHAMADO PARA O VALOR = {cls.valor}',60,2)

    @staticmethod
    def metodo_static():
        printTextCentralized(f'MÉTODO ESTÁTICO CHAMADO',60,2)

obj = MinhaClasse('Classe de exemplo'.upper())
obj.metodo_instancia()
MinhaClasse.metodo_class()
MinhaClasse.metodo_static()

class Carro:
    def __init__(self,marca,modelo,ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(',')
        return cls(marca, modelo, int(ano))

configuracao1 = 'Toyota,Corolla,2022'
carro1 = Carro.criar_carro(configuracao1)


jumpLine()
imprimirLinha(2,20)
printTextCentralized(f'Marca: {carro1.marca} | Modelo: {carro1.modelo} | Ano: {carro1.ano}',60,2)
imprimirLinha(2,20)

class Matematica:

    @staticmethod
    def somar(a, b):
        jumpLine()
        print(f'A soma entre {a} e {b} = {a+b}')

Matematica.somar(5,8)