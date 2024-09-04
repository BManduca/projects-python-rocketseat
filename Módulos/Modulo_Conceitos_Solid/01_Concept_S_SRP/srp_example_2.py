'''
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

from abc import ABC, abstractmethod
from os import system
import time

colors=('\033[m',      # 0 - sem cores
        '\033[0;31m',  # 1 - vermelho
        '\033[0;32m',  # 2 - verde
        '\033[0;33m',  # 3 - amarelo
        '\033[0;34m',  # 4 - azul
        '\033[0;35m',  # 5 - roxo
        '\033[7;30m'   # 6 - branco
        )

def printLine20(cor=0):
   print(colors[cor], end='')
   print('-=-'*20)
   print(colors[0], end='')

def printLine28(cor=0):
   print(colors[cor], end='')
   print('-=-'*28)
   print(colors[0], end='')

def messageCentralized(msg, wid: int):
   tam = len(msg)
   space = (wid - tam) // 2
   text = ' ' * space + msg + ' ' * space
   #  se o texto não puder ser centralizado perfeitamente, ajuste uma posição para a direita

   if len(text) < wid:
      text +=''

   return text

def printTextCentralized(msg, wid, cor=0):
   message = messageCentralized(msg, wid)
   print(colors[cor], end='')
   print(message)
   print(colors[0], end='')

def showMenu():
   printLine28(4)
   printTextCentralized('PROGRAMA PARA REALIZAR CÁLCULOS COM BASE EM FORMAS GEOMÉTRICAS', 80, 4)
   print()
   printTextCentralized('SELECIONE UMA OPÇÃO: ', 80, 4)
   print(' ')
   printTextCentralized('1 - QUADRADO', 80, 4)
   printTextCentralized('2 - TRIÂNGULO', 80, 4)
   printTextCentralized('3 - RETÂNGULO', 80, 4)
   printTextCentralized('0 - FINALIZAR PROGRAMA', 80, 4)
   printLine28(4)

class HandleShapes(ABC):
   
   @abstractmethod
   def calculate_area(self, comprimento_lado: int):
      pass
   
   @abstractmethod
   def calculate_perimeter(self, comprimento_lado: int):
      pass
   
class GeometricShapeSquare(HandleShapes):
   
   def calculate_area(self, comprimento_lado) -> float:
      res = comprimento_lado * 2
      printTextCentralized(f'A área do quadrado é igual a {res}', 80, 2)
   
   def calculate_perimeter(self, comprimento_lado) -> float:
      res = comprimento_lado * 4
      printTextCentralized(f'O perímetro do quadrado é igual a {res}', 80, 2)


def main():
   while True:
      showMenu()
      print('\n')

      textChoice = 'ESCOLHA UMA DAS FORMAS GEOMETRICAS (0 - PARA FINALIZAR): '

      opt = int(input(f'{textChoice}'))

      if opt == 1:
        side_square_width = int(input('\nInsira o valor do lado do quadrado: '))
        print('\n')
        geometrica_shape_square = GeometricShapeSquare()
        printLine28()
        geometrica_shape_square.calculate_area(side_square_width)
        geometrica_shape_square.calculate_perimeter(side_square_width)
        printLine28()
        time.sleep(5)
        system('clear')
      elif opt == 0:
         print('\n')
         printLine28(1)
         printTextCentralized('FINALIZANDO PROGRAMA...', 80, 1)
         printLine28(1)
         time.sleep(2)
         break
      else:
         print('\n')
         printTextCentralized('OPÇÃO INVÁLIDA! POR FAVOR,', 80, 1)
         printTextCentralized('INSIRA NOVAMENTE UMA OPÇÃO DO MENU!', 80, 1)
         print('\n')
         time.sleep(5)
         system('clear')
         

if __name__ == "__main__":
   main()