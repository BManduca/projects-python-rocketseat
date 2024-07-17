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
    bank_payment_id = db.Column(db.String(200), nullable=True)
    qr_code = db.Column(db.String(100), nullable=True)
    expiration_date = db.Column(db.DateTime) # AAAA-MM-DD HH:MM:SS

    def to_dict(self):
        return {
            'id': self.id,
            'value': self.value,
            'paid': self.paid,
            'bank_payment_id': self.bank_payment_id,
            'qr_code': self.qr_code,
            'expiration_date': self.expiration_date
        }