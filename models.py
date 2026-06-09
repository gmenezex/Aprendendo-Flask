# Reponsavel por guardar os modelos do banco de dados
from db import db
from flask_login import UserMixin

class Contato(db.Model):
  __tablename__ = 'contatos'

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(50), nullable=False)
  telefone = db.Column(db.Integer, nullable=False)

  def __repr__(self):
    return f"<{self.nome}>"


class Usuario(UserMixin,db.Model):
  __tablename__ = 'usuarios'

  id = db.Column(db.Integer, primary_key=True)

  nome = db.Column(db.String(30), unique=True)

  senha = db.Column(db.String())