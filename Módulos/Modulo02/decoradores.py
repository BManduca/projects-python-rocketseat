from typing import Any
from modules.styleModule import jumpLine, printTextCentralized, imprimirLinha

def meu_decorador(func):
    def wrapper():
        jumpLine()
        printTextCentralized('ANTES DA MINHA FUNÇÃO SER CHAMADA',60,4)
        func()
        printTextCentralized('DEPOIS DA MINHA FUNÇÃO SER CHAMADA',60,4)
    return wrapper

@meu_decorador
def minha_funcao():
    printTextCentralized('MINHA FUNÇÃO FOI CHAMADA!',60,3)

minha_funcao()


# decorador como classe -> utilizado geralmente em bibliotecas

class MeuDecoradorDeClasses:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> Any:
        jumpLine()
        printTextCentralized('ANTES DA FUNÇÃO SER CHAMADA (DECORADOR DE CLASSE)',60,4)
        self.func()
        printTextCentralized('DEPOIS DA FUNÇÃO SER CHAMADA (DECORADOR DE CLASSE)',60,4)

@MeuDecoradorDeClasses
def minha_segunda_funcao():
    printTextCentralized('MINHA SEGUNDA FUNÇÃO',60,4)

minha_segunda_funcao()