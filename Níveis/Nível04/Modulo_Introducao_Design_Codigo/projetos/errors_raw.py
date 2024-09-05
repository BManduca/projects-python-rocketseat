
class HttpUnprocessableentityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422

try:
    print('ESTOU NO BLOCO TRY')
    raise HttpUnprocessableentityError('ESTOU LANÇANDO A EXCEPTION!')
except Exception as exception:
    print('\nESTOU NO TRATAMENTO DE ERRO!')
    print(f'\nErro: {exception.name}')
    print(f'Status_code: {exception.status_code}')