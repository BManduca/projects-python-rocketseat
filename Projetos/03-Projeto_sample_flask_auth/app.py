from flask import Flask, jsonify, request
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

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
login_manager.login_view = 'login'
# Session <- conexão ativa.

'''
    Toda vez que for preciso recuperar informação do user,
    flask-login é capaz de usar o load_user, para recuperar o objeto cadastrado 
    no banco de dados, o registro completo, que vai vir no formato da
    classe
'''
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# 
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:
        # login success
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({'message': 'AUTENTICAÇÃO REALIZADA COM SUCESSO!'})
    
    return jsonify({'message': 'CREDENCIAIS INVÁLIDAS!'}), 400

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'LOGOUT REALIZADO COM SUCESSO!'})

@app.route('/user', methods=['POST'])
@login_required
def create_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'USUÁRIO CADASTRADO COM SUCESSO!'})

    return jsonify({'message': 'DADOS INVÁLIDOS!'}), 400

@app.route('/hello-word', methods=['GET'])
def hello_word():
    return 'Hello World'

if __name__ == '__main__':
    app.run(port=8000, debug=True)
