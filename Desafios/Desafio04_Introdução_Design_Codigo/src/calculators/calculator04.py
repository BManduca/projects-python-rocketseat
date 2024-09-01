from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from flask import request as FlaskRequest
from typing import Dict, List
'''

  CALCULADORA

  - ADICIONAR UMA ROTA PARA RETORNAR MÉDIA ENTRE UMA LISTA DE NÚMEROS 
  FORNECIDA EM UMA REQUISIÇÃO POST

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

def imprimirMensagem(msg, cor=0):
    print(colors[cor], end='')
    print(f'{msg:^60}')
    print(colors[0], end='')

class Calculator4:

  def __init__(self, driver_handler: DriverHandlerInterface) -> None:
    self.__driver_handler = driver_handler


  def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
    body = request.json

    input_data = self.__validate_body(body)
    average = self.__calculate_average(input_data)

    response_formatted = self.__format_response(average)

    return response_formatted

  # validating the body passed on in the call
  def __validate_body(self, body: Dict) -> List[float]:

    if 'numbers' not in body:
      raise HttpUnprocessableEntityError('BODY MAL FORMATADO')

    input_data = body['numbers']
    return input_data
  
  def __calculate_average(self, numbers: List[float]) -> float:
    '''
      another way to perform the average

      average = sum(numbers) / len(numbers)

      response = self.__format_response(average)

      return response
    '''
    average = self.__driver_handler.average(numbers)
    return average
  
  def __format_response(self, average: float) -> Dict:
    return {
      'data': {
        'Calculator': 4,
        'average': round(average, 2)
      }
    }
  
