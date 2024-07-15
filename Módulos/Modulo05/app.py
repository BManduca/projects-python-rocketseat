from flask import Flask, jsonify

app = Flask(__name__)

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
    return f'PAGAMENTO PIX {payment_id}'


if __name__ == '__main__':
    app.run(debug=True)