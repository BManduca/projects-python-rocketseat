from flask import Flask, jsonify
'''
    permite que seja instanciado o DB em outro arquivo
    e assim permite que seja modelado o model de pagamento em outra classe
'''
from repository.database import db
from db_models.payment import Payment

app = Flask(__name__)

# CONFIGS PARA SQLITE -> DB EM ARQUIVOS
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'MY_SECRET_KEY_WEBSOCKET'
db.init_app(app)


# ROTA PARA CRIAÇÃO DE UM PAGAMENTO
@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    return jsonify({'message': 'THE PAYMENT HAS BEEN CREATED.'})

# ROTA PARA CONFIRMAÇÃO DO PAGAMENTO
@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({'message': 'THE PAYMENT HAS BEEN CONFIRMED.'})

# ROTA PARA GERAR INFORMAÇÕES DE PAGAMENTO
@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return 'PAGAMENTO PIX'


if __name__ == '__main__':
    app.run(port=8000, debug=True)