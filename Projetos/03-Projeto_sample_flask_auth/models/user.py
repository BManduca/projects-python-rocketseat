from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    #  id -> int, username -> text, password -> text
    #  primary_key -> chave que identifica os registros na tabela e esta é única
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)