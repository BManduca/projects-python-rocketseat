'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

----------------------------------------------------------------

  Colors em python, este código se inicia com \033[

  0 => none (sem estilo)
  1 => bold(negrito)
  2 => Fraco
  3 => itálico
  4 => underline (sublinhado)
  7 => negative (inverter as configurações Fundo vai pra letra e letra fundo)

  ----------------------------------------------------------------
  Cores para o texto:
  30 => Branco
  31 => Vermelho
  32 => Verde
  33 => Amarelo
  34 => Azul
  35 => Magenta
  36 => Ciano
  37 => Cinza

  ----------------------------------------------------------------
  Cores para o fundo:
  40 = Branco
  41 = Vermelho
  42 = Verde
  43 = Amarelo
  44 = Azul
  45 = Magenta
  46 = Ciano
  47 = Cinza

  ----------------------------------------------------------------

'''

colors=('\033[m',      # 0 - sem cores
        '\033[0;31m',  # 1 - vermelho
        '\033[0;32m',  # 2 - verde
        '\033[0;33m',  # 3 - amarelo
        '\033[0;34m',  # 4 - azul
        '\033[0;35m',  # 5 - roxo
        '\033[7;30m'   # 6 - branco
        )

from abc import ABC, abstractmethod

def printLine(cor=0):
    print(colors[cor], end='')
    print('-=-'*32)
    print(colors[0], end='')

def printMessage(msg, cor=0):
    print(colors[cor], end='')
    print(f'{msg:^100}')
    print(colors[0], end='')

# create interface
class AprovaExame(ABC):
    @abstractmethod
    def aprovar_solicitacao_exame(self, exame):
        pass

    @abstractmethod
    def verifica_condicoes_exame(self, exame):
        pass

class AprovarExameSangue(AprovaExame):
    def aprovar_solicitacao_exame(self, exame) -> None:
        if self.verifica_condicoes_exame(exame) == 'S':
            printMessage('Exame sanguínio aprovado com sucesso...', 2)

    def verifica_condicoes_exame(self, exame) -> str:
        printMessage('Para Realização do Exame de Sangue, o índividuo: ', 3)
        print()
        printMessage(' - Realizar uma dieta leve por 5 dias.', 1)
        printMessage(' - Não deve ingerir bebida alcoólica até 72 horas antes.', 1)
        printMessage(' - Não é aconselhado a prática de exercícios físicos intensos até 24 horas antes do exame.', 1)
        printMessage(' - Realizar um Jejum em que pode variar entre 0 e 14 horas, para todas as faixas etárias.', 1)
        
        print()
        ans = str(input('   ==> O Paciente está apto para realizar o exame? (S/N):  ')).upper()
        print()
        while ans not in 'SN':
            ans = str(input('   ==> O Paciente está apto para realizar o exame? (S/N):  ')).upper()
            print()

        if ans == 'S':
            printMessage('O Paciente está apto para realizar o exame\n', 2)
        else:
            printMessage('O Paciente não está apto para realizar o exame', 1)

        return ans


class AprovarRaioX(AprovaExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verifica_condicoes_exame(exame) == 'S':
            printMessage('Exame de raio-x aprovado com sucesso...', 2)

    def verifica_condicoes_exame(self, exame):
        printMessage('Para Realização do Exame de Raio X, o índividuo deve: ', 1)
        printMessage(' - Remover joías e/ou acessórios que possam atrapalhar o exame.', 1)
        printMessage(' - Prender o cabelo antes do exame.', 1)

        print()
        ans = str(input('   ==> O Paciente está apto para realizar o exame? (S/N):  ')).upper()
        print()
        while ans not in 'SN':
            ans = str(input('   ==> O Paciente está apto para realizar o exame? (S/N):  ')).upper()
            print()

        if ans == 'S':
            printMessage('O Paciente está apto para realizar o exame\n', 2)
        else:
            printMessage('O Paciente não está apto para realizar o exame', 1)

        return ans

class Exame:
    def __init__(self, tipo):
        self.tipo = tipo



    

exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

aprovar_exame_sangue = AprovarExameSangue()
aprovar_raio_x = AprovarRaioX()

printLine(2)
print()
aprovar_exame_sangue.aprovar_solicitacao_exame(exame_sangue)
print()
printLine(2)
print()

print()
printLine(2)
print()
aprovar_raio_x.aprovar_solicitacao_exame(exame_raio_x)
print()
printLine(2)

