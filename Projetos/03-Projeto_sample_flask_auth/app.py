from flask import Flask, jsonify, request
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import bcrypt

app = Flask(__name__)
'''
    - necessário para a área de autenticação
    - utilizado pelo flask para proteger as informações armazenadas
'''
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mand_42#21@127.0.0.1:3307/flask-crud'

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

        if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({'message': 'AUTENTICAÇÃO REALIZADA COM SUCESSO!'})
    
    return jsonify({'message': 'CREDENCIAIS INVÁLIDAS!'}), 400

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'LOGOUT REALIZADO COM SUCESSO!'})


# REGISTER
@app.route('/user', methods=['POST'])
@login_required
def create_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username and password:
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        user = User(username=username, password=hashed_password, role='user')
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'USUÁRIO CADASTRADO COM SUCESSO!'})

    return jsonify({'message': 'DADOS INVÁLIDOS!'}), 400


# READ USER
@app.route('/user/<int:id_user>', methods=['GET'])
@login_required
def read_user(id_user):
    # user = User.query.filter_by(id_user)
    user = User.query.get(id_user)

    if user:
        return {'username': user.username}
    
    return jsonify({'message': 'USUÁRIO NÃO ENCONTRADO'}), 404


# UPDATE
@app.route('/user/<int:id_user>', methods=['PUT'])
@login_required
def update_user(id_user):
    data = request.json
    user = User.query.get(id_user)

    if id_user != current_user.id and current_user.role == 'user':
        return jsonify({'message': 'OPERAÇÃO NÃO PERMITIDA!'}), 403
    
    if user and data.get('password'):
        user.password = data.get('password')
        db.session.commit()

        return jsonify({'message': f'USUÁRIO {id_user} ATUALIZADO COM SUCESSO!'})
    
    return jsonify({'message': 'USUÁRIO NÃO ENCONTRADO!'}), 404


# DELETE
@app.route('/user/<int:id_user>', methods=['DELETE'])
@login_required
def delete_user(id_user):
    user = User.query.get(id_user)

    if current_user.role != 'admin':
        return jsonify({'message': 'OPERAÇÃO NÃO PERMITIDA!'}), 403
    if id_user == current_user.id:
        return jsonify({'message': 'DELEÇÃO NÃO PERMITIDA!'}), 403
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': f'USUÁRIO {id_user} DELETADO COM SUCESSO!'})
    
    return jsonify({'message': 'USUÁRIO NÃO ENCONTRADO!'}), 404

if __name__ == '__main__':
     app.run(port=8000, debug=True)