from flask import Flask
# Evita que caracteres especiais sejam enviados pela rota
from markupsafe import escape

#Iniciando o flask
app = Flask(__name__)

# A rota inicial
@app.route('/')
def index():
  return 'Olá, mundo!'

# Acessando uma rota chamada teste
@app.route('/teste')
def teste():
  return 'Testando uma nova rota'

# Acessando uma roto com parametro
@app.route('/ola/<nome>')
def ola(nome):
  nome = escape(nome)
  return f'<h1>Olá, {nome}</h1>'

# Fazendo o flask rodar somente 1 vez
if __name__ == '__main__':
  app.run(debug=True)