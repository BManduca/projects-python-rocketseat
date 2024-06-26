from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
'''
    - necessário para a área de autenticação
    - utilizado pelo flask para proteger as informações armazenadas
'''
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# criando a conexao da aplicação com o banco | instância do SQLAlchemy
db = SQLAlchemy(app)

@app.route('/hello-word', methods=['GET'])
def hello_word():
    return 'Hello World'

if __name__ == '__main__':
    app.run(port=8000, debug=True)
