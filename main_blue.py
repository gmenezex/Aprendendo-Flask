from flask import Flask
from blueprints.menssagens.menssagens import menssagens_bp
from blueprints.calculadora.calculadora import calculadora_bp

app = Flask(__name__)
app.register_blueprint(menssagens_bp, url_prefix='/menssagens')
app.register_blueprint(calculadora_bp)

@app.route('/')
def index():
  return 'Olá!'

if __name__ == '__main__':
  app.run(debug=True)