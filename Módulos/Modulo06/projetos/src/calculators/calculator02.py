from flask import request as FlaskRequest
from typing import Dict, List

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
        print(body)
        input_data = self.__validate_body(body)
        print(input_data)

    def __validate_body(self, body: Dict) -> List[float]:
        if 'numbers' not in body:
            raise Exception('BODY MAL FORMATADOR!')
        
        input_data = body['numbers']
        return input_data