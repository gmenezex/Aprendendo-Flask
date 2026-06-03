from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  dados = {
    'nome': 'Gabriel',
    'sobrenome': 'Menezes',
    'idade': 28
  }
  return render_template('exemplo_template.html', dados=dados, nome='Gabriel')

if __name__ == '__main__':
  app.run(debug=True)