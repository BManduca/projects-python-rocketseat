from .calculator01 import Calculator1
from pytest import raises
from typing import Dict

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={
        'number': 1
    })

    calculator01 = Calculator1()

    response = calculator01.calculate(mock_request)

    # RESPONSE FORMAT
    assert 'data' in response
    assert 'Calculator' in response['data']
    assert 'result' in response['data']

    # RESPONSE ASSERT
    assert response['data']['Calculator'] == 1
    assert response['data']['result'] == 14.25

def test_calculate_with_body_error():
    mock_request = MockRequest(body={
        'something': 1
    })

    calculator01 = Calculator1()

    '''
        verificando se caso exista alguma exceção
        neste tipo de execução -> calculator01.calculate(mock_request)
    '''
    with raises(Exception) as exceptionInfo:
        calculator01.calculate(mock_request)

    assert str(exceptionInfo.value) == 'BODY MAL FORMATADO!'
