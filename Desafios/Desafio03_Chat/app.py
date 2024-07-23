from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template(
        'index.html'
    )

# WebSockets
@socketio.on('message') # aguardando um evento de mensagem
def handle_message(message):
    '''
        função emit é um evento SocketIO para um ou mais clientes 
        conectados. Um blob JSON pode ser anexado ao evento como 
        carga útil. Esta função pode ser usada fora de um contexto 
        de evento SocketIO, por isso é apropriado usar quando o 
        servidor é o originador de um evento, fora de qualquer 
        contexto do cliente, como em um manipulador de 
        solicitação HTTP regular ou em uma tarefa em segundo 
        plano.
    '''
    # print(f'MESSAGE: {message}')
    emit('message', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, port=8000,debug=True)