'''

    TERCEIRA CALCULADORA

    - N NÚMEROS SÃO COLOCADOS COMO ENTRADA
    * CASO A VARIÂNCIA DE TODOS ESSES NÚMEROS FOR MENOR QUE 
    A MULTIPLICAÇÃO DELES, É APRESENTADO UMA INFORMAÇÃO DE SUCESSO AO 
    USUÁRIO

    - CASO CONTRÁRIO, É APRESENTADO UMA INFORMAÇÃO DE FALHA

    OBS.: PARA O CÁCULO DE VARIÂNCIA, UTILIZE O MÉTODO 'VAR' DA LIB numpy

'''

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List 

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

    def validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body:
            raise Exception('BODY MAL FORMATADO!')
        
        input_data = body['numbers']
        return input_data
    
    def calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler