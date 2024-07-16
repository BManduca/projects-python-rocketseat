from repository.database import db

'''
    Class Payment -> Tabela que vai armazenar todos os pagamentos 
    que serão criados no nosso sistema e para ter todas as funcionalidades
    do Flask SQLAlchemy, temos que herdar do db.Model, que é classe presente dentro
    do objeto criado dentro do arquivo database.py (Herança)
'''

class Payment(db.Model):
    # id, value, paid, bank_payment_id, qr_code, expiration_date.
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qr_code = db.Column(db.String(100), nullable=True)
    expiration_date = db.Column(db.DateTime) # AAAA-MM-DD HH:MM:SS