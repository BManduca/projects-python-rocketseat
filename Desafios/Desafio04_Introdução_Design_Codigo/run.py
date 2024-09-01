from src.main.server.server import app

if __name__ == '__main__':
    # Setando a porta do Flask para rodar o server
    app.run(port=8000, debug=True)