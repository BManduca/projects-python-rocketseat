'''

    TERCEIRA CALCULADORA

    - N NÚMEROS SÃO COLOCADOS COMO ENTRADA
    * CASO A VARIÂNCIA DE TODOS ESSES NÚMEROS FOR MENOR QUE 
    A MULTIPLICAÇÃO DELES, É APRESENTADO UMA INFORMAÇÃO DE SUCESSO AO 
    USUÁRIO

    - CASO CONTRÁRIO, É APRESENTADO UMA INFORMAÇÃO DE FALHA

    OBS.: PARA O CÁCULO DE VARIÂNCIA, UTILIZE O MÉTODO 'VAR' DA LIB numpy

    
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

Exemplo:
Teste ----> "\033[0;30;41mTeste\033[m"

Teste ----> "\033[4;33;44mTeste\033[m"

Teste ----> "\033[1;35;43mTeste\033[m"

Teste ----> "\033[30;42mTeste\033[m"

Teste ----> "\033[mTeste\033[m (padrão do terminal)"

Teste ----> "\033[7;30mTeste\033[m (letra preta)"
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
    print(f'{msg}')
    print(colors[0], end='')

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json

        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)

        self.__verify_result(variance, multiplication)

        formatted_response = self.__format_response(variance)

        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body:
            raise HttpUnprocessableEntityError('BODY MAL FORMATADO!')
        
        input_data = body['numbers']
        return input_data
    
    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1

        for num in numbers: multiplication *= num

        return multiplication
    
    def __verify_result(self, variance: float, multiplication: float) -> None:

        if variance < multiplication:
            # print('\nSUCESSO: Variância é menor que a multiplicação!')
            imprimirMensagem('  ==> SUCESSO', 2)
        else:
            raise HttpBadRequestError('Falha no processo: Variância é maior que a multiplicação!')
        

    def __format_response(self, variance: float) -> Dict:
        return {
            'data': {
                'Calculator': 3,
                'value': variance,
                'success': True
            }
        }