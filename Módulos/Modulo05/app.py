from flask import Flask, jsonify, request, send_file, render_template
'''
    permite que seja instanciado o DB em outro arquivo
    e assim permite que seja modelado o model de pagamento em outra classe
'''
from repository.database import db
from db_models.payment import Payment
from datetime import datetime, timedelta
from payments.pix import Pix
from flask_socketio import SocketIO

app = Flask(__name__)

# CONFIGS PARA SQLITE -> DB EM ARQUIVOS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'MY_SECRET_KEY_WEBSOCKET'
db.init_app(app)
socketio = SocketIO(app)


# ROTA PARA CRIAÇÃO DE UM PAGAMENTO
@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    data = request.get_json()

    #validações
    if 'value' not in data:
        return jsonify({'message':'INVALID VALUE'}), 400
    
    expiration_date = datetime.now() + timedelta(minutes=30)

    new_payment = Payment(
        value=data['value'], 
        expiration_date=expiration_date
    )

    pix_obj = Pix()
    data_payment_pix = pix_obj.create_payment() # acesso ao bank_payment_id e o qr_code
    new_payment.bank_payment_id = data_payment_pix['bank_payment_id']
    new_payment.qr_code = data_payment_pix['qr_code_path']


    db.session.add(new_payment)
    db.session.commit()
    
    return jsonify({'message': 'THE PAYMENT HAS BEEN CREATED.',
                    'payment': new_payment.to_dict()})

# ROTA PARA RETORNAR IMAGEM(QRCODE) PARA O USUARIO
@app.route('/payments/pix/qr_code/<file_name>', methods=['GET'])
def get_image(file_name):
    return send_file(f'static/img/{file_name}.png', mimetype='image/png')



# ROTA PARA CONFIRMAÇÃO DO PAGAMENTO
@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    data = request.get_json()

    # validations
    if 'bank_payment_id' not in data and 'value' not in data:
        return jsonify({'message': 'DADOS DE PAGAMENTO INVÁLIDOS!'}), 400

    # verificar qual pagamento precisa ser 'recuperado'
    # A notificao financeira de confirmação ira usar o id da instituicao vinculada ao pagamento
    payment = Payment.query.filter_by(bank_payment_id=data.get('bank_payment_id')).first()

    if not payment or payment.paid:
        return jsonify({'message': 'PAGAMENTO NÃO REALIZADO!'}), 404
    
    # value
    if data.get('value') != payment.value:
        return jsonify({'message': 'DADOS DE PAGAMENTO INVÁLIDOS!'}), 400
    
    payment.paid = True
    db.session.commit()
    socketio.emit(f'payment-confirmed-{payment.id}')

    return jsonify({'message': 'O PAGAMENTO FOI REALIZADO COM SUCESSO!'})

# ROTA PARA GERAR INFORMAÇÕES DE PAGAMENTO
@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    payment = Payment.query.get(payment_id)

    if payment.paid:

        return render_template(
            'confirmed_payment.html',
            payment_id = payment.id,
            value = payment.value
        )

    return render_template(
        'payment.html',
        payment_id = payment.id,
        value = payment.value,
        host = 'http://127.0.0.1:8000/',
        qr_code = payment.qr_code
    )

# WebSockets
@socketio.on('connect') # aguardar um evento
def handle_connect():
    print('CLIENT CONNECTED TO THE SERVER!')

if __name__ == '__main__':
    socketio.run(app, port=8000, debug=True)