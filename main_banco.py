from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Configurando o banco de dados e informando qual vamos utilizar (aqui vai ser o SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
#Representa o banco de dados
db = SQLAlchemy()
db.init_app(app)

#Criação da tabela usuarios do banco de dados.
class Usuario(db.Model):
  __tablename__ = 'usuarios'

  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(40), nullable=False, unique=True)

  # Esse repr vai apresentar o valor que está informando no return
  def __repr__(self):
    return f"<{self.nome}>"


@app.route('/')
def index():
  return 'Olá'

if __name__ == '__main__':
  #Criando o banco de dados
  with app.app_context():
    #Inserindo dados no banco de dados e na tabela usuario
    '''
    user = Usuario(nome='Menezes')
    db.session.add(user)
    db.session.commit()
    db.create_all()
    
    #Consultando dados no banco, puxando todos os dados
    usuarios = db.session.query(Usuario).all()
    for usuario in usuarios:
      print(usuario.nome)
    
    #Consultando somente 1 registro no banco de dados
    user = db.session.query(Usuario).filter_by(nome='Gabriel').first()
    print(user.id, user.nome)
    
    #Como alterar dados no banco
    user = db.session.query(Usuario).filter_by(nome='Gabriel').first()
    user.nome = 'Joãozinho'
    db.session.commit()
    
    #Como excluir um dado do banco
    user = db.session.query(Usuario).filter_by(nome='Joãozinho').first()
    db.session.delete(user)
    db.session.commit()
    '''
  app.run(debug=True)