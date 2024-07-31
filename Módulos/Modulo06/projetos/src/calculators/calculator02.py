from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler

'''
    SEGUNDA CALCULADORA

    - N NÚMEROS ENVIADOS
    - TODOS ESSES NÚMEROS SÃO MULTIPLICADOS POR 11 E ELEVADOS A POTENCIA DE 0.95
    - POR FIM, É RETIRADO O DESVIO PADRÃO DESSES RESULTADOS E RETORNADO O INVERSO DESSE 
    VALOR (1/RESULT)

    DICA: UTILIZE A LIB NUMPY PARA CALCULAR O DESVIO PADRÃO

'''

class Calculator2:

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)

        formated_response = self.__format_response(calculated_number)

        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body:
            raise Exception('BODY MAL FORMATADOR!')
        
        input_data = body['numbers']
        return input_data
    
    def __process_data(self, input_data: List[float]) -> float:
        # criando uma instância do nosso NumpyHandler
        numpy_handler = NumpyHandler()
        first_process_result = [
            (num * 11) ** 0.95 for num in input_data
        ]
        result = numpy_handler.standard_derivation(first_process_result)
        return 1/result
    
    def __format_response(self, calculated_number: float) -> Dict:
        return {
            'data': {
                'Calculator': 2,
                'result': round(calculated_number, 2)
            }
        }