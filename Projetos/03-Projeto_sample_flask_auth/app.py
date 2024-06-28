from flask import Flask, jsonify, request
from models.user import User
from database import db
from flask_login import LoginManager

app = Flask(__name__)
'''
    - necessário para a área de autenticação
    - utilizado pelo flask para proteger as informações armazenadas
'''
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

# view login

# Session <- conexão ativa.

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:
        # login success
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            return jsonify({'message': 'AUTENTICAÇÃO REALIZADA COM SUCESSO!'})
    
    return jsonify({'message': 'CREDENCIAIS INVÁLIDAS!'}), 400

@app.route('/hello-word', methods=['GET'])
def hello_word():
    return 'Hello World'

if __name__ == '__main__':
    app.run(port=8000, debug=True)
