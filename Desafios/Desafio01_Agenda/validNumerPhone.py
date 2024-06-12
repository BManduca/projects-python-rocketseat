import time
import sys

def validationPhone(number_phone):

    try:
        if len(number_phone) != 11:
            raise ValueError
        else:
            # caso tenha letrar ou caracteres, causa um ValueError
            number_phone = int(number_phone)

    except ValueError:
        if len(number_phone) == 0:
            print('VOCÊ NÃO INSERIU O TELEFONE!')
            time.sleep(3)
            sys.exit('ENCERRANDO SISTEMA DE CADASTRO...')
        else:
            print('TELEFONE INVÁLIDO! O TELEFONE PRECISA TER 11 DÍGITOS!')
            time.sleep(3)
            sys.exit('ENCERRANDO SISTEMA DE CADASTRO...')
        

def printFormattedPhone(formatted_number):
    # caso tenha letrar ou caracteres, causa um ValueError
    formatted_number = int(formatted_number)
    formatted_number = str(formatted_number)

    phoneNumber = f'({formatted_number[0:2]}){formatted_number[2:7]}-{formatted_number[7:]}'
    print(phoneNumber)