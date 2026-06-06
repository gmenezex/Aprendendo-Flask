from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
  lista_numeros = []
  if request.method == 'POST':
    numeros = request.form['numerosForm']
    lista_numeros = [int(numeros[n]) for n in range(len(numeros))]
  pares = [numero for numero in lista_numeros if numero % 2 == 0]
  impares = [numero for numero in lista_numeros if numero % 2 > 0]

  return render_template('par_impar.html', lista_numeros=lista_numeros, pares=pares, impares=impares)

if __name__ == '__main__':
  app.run(debug=True)