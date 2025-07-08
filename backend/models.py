from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(200), nullable=False)
