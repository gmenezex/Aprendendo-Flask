from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  frutas = ['Maça', 'Banana', 'Manga']
  dados = {
    'nome': 'Gabriel',
    'sobrenome': 'Menezes',
    'idade': 28
  }
  return render_template('exemplo_template.html', dados=dados, nome='Gabriel', frutas=frutas)

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
  if request.method == 'POST': 
    nome = request.form['nomeForm']
    email = request.form['emailForm']
    print(f'Método usado: {request.method}')
    print(nome, email)
  return render_template('formulario.html')

if __name__ == '__main__':
  app.run(debug=True)