from typing import Dict
'''
    no final da definição da função,
    estou indicando qual o retorno esperado para a função.

    neste exemplo, um Dict
'''
def add(elem1: int, elem2: float) -> Dict:
    response = elem1 + elem2
    return {
        'sum': response
    }

val1 = add(5, 3.45)

print(val1)

# typing => int, float, str, bool = True/False
# estrutura de dados => Dict, list, tuple