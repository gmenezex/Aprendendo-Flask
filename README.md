# Aprendendo-Flask
Repositório feito para aprender o Flask

Vamos usar a extensão 
Jinja Snippets > para facilitar no html

## 1° Instalar um ambiente virtual, ativar ele e instalar o Flask

### Ambiente virtual > python -m venv .venv
#### Ativando: ".\.venv\Scripts\activate"

### Como instalar o flask?
#### pip install flask


## Como criar uma rota no Flask?
### Exemplo:
@app.route('/')
def index():
  return 'Olá, mundo!'

## Usando o template do Flask?
importando do proprio flask o render_template

Obs: Tem que ser criadouma pasta com o nome templates, pois ele busca os arquivos 
direto nessa pasta
Exemplo de como chamar o arquivo:
@app.route('/')
def index():
  return render_template('exemplo_template.html')

Enviando com parametro:
@app.route('/')
def index():
  return render_template('exemplo_template.html', nome="Gabriel")

Criando uma condição no html:
"<p>Olá {{nome|default('sem nome')}}</p>"
Caso a variavel nome não seja informada no render_template, ele vai renderizar na tela
a informação 'sem nome'

Passando uma imagem para o html:
Temos que criar a pasta chamada static e dentro dela vamos colocar as imagens.
(<img src="{{url_for('static', filename='cachorro.jpg')}}" alt="">')
Passamos o endereço da imagem dessa forma

Controle de estrutura (IF) dentro do html:
(
    {% if dados.idade >= 18 %}
    <p>Você é maior de idade</p>
  {% else %}
    <p>Você é menor de idade</p>
  {% endif %}
)

Usando FOR no html:
(
  <ul>
    {% for fruta in frutas %}
    <li>{{fruta}}</li>
    {% else %}
    <p>Lista vazia</p>
    {% endfor %}
  </ul>
)
---------------------------------------------
Enviando dados via POST de um Formulario.html:
Temos que importar o request primeiro.

Dentro da função, vamos colocar metodo POST e também vamos verificar se foi enviado o POST.
Vamos pegar os dados do formulario pela tag name que fica nos inputs, exemplo:

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
  if request.method == 'POST': 
    nome = request.form['nomeForm']
    email = request.form['emailForm']

----------------------------------------------
Base de html para todas as paginas:
Dentro do base.html usamos o block conteudo, exemplo::
(
<body>
  <header>
    <a href="/">Home</a>
    <a href="/contato">Contato</a>
  </header>
  {% block conteudo %}
    
  {% endblock %}
</body>
)

E a página que for utilizar por exemplo o Header, tem que usar o extends, exemplo:
(
{% extends 'base.html' %}
{% block conteudo %}
  <h1>Bem-Vindo</h1>
{% endblock %}
)
---------------------------------------------
Banco de dados SQLAlchemy
Vamos rodar primeiro o "pip install flask-sqlalchemy". Ele é uma ORM.
Depois de rodar, é preciso importar:
from flask_sqlalchemy import SQLAlchemy

----------------------------------------------
Sistema de login !
Temos que instalar a biblioteca do Flask login
pip install flask-login
depois importar 
from flask_login import LoginManager

Biblioteca para criptografar senhas
import hashlib