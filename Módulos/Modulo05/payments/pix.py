# repositorio organizar classes de pagamentos

import uuid
import qrcode

class Pix():
    def __init__(self):
        pass

    def create_payment(self):
        '''
            criando um ID que simula o pagamento na instituição financeira
            o random uuid retorna um objeto e para converter o mesmo, basta usar str(), 
            envolvendo a geração da chave ID de maneira randômica
        '''
        bank_payment_id = str(uuid.uuid4())

        #qr_code
        hash_payment = f'hash_payment_{bank_payment_id}'

        # cmd make create image
        img = qrcode.make(hash_payment)

        # save image -> archive png
        img.save(f'static/img/qr_code_payment_{bank_payment_id}.png')

        return {
            'bank_payment_id': bank_payment_id,
            'qr_code_path': f'qr_code_payment_{bank_payment_id}'
        }