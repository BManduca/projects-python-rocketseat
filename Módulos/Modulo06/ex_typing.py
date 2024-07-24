from typing import Dict

def add(elem1: int, elem2: float) -> Dict:
    response = elem1 + elem2
    return {
        'sum': response
    }

val1 = add(5, 3.45)

print(val1)

# int, float, str, bool = True/False
# Dict, list, tuple